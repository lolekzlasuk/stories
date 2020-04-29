from django.shortcuts import render, get_object_or_404,redirect
from .forms import UserForm,EventForm,StoryForm, StorylineForm, EventCommentForm, UserProfileForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Story,Storyline,StoryEvent, UserProfile
from django.utils import timezone


class IndexView( TemplateView):
    template_name = 'index.html'


class StoryListView(LoginRequiredMixin, ListView):
    model = Story

    def get_queryset(self):
        return Story.objects.order_by('-created_date')

class StoryDetailView(LoginRequiredMixin, DetailView):
    # model = Story
    queryset = Story.objects.all()

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
# class EventCreate(CreateView):
#     model = StoryEvent
#     fields = ['author']

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('myapp:story_list'))

            else:
                return HttpResponse('account no active')
        else:
            print('failed login detected')
            print('username: {} and password {}'.format(username,password))
            return HttpResponse('invalid login details supplied')

    else:
        return render(request,'login.html',{})

@login_required
def addevent(request,pk):
    storyline = get_object_or_404(Storyline, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():

            event = form.save(commit=False)
            event.author = User.objects.get(username=request.user.username)
            event.storyline = storyline

            form.save()
            return redirect('myapp:story_detail',pk=storyline.story.pk)
    else:
        form = EventForm()
    return render(request,'myapp/event_form.html',{'form':form})


@login_required
def addstoryline(request,pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == 'POST':
        form = StorylineForm(request.POST)
        if form.is_valid():
            storyline = form.save(commit=False)
            storyline.author = User.objects.get(username=request.user.username)
            storyline.story = story
            form.save()
            return redirect('myapp:story_detail',pk=story.pk)
    else:
        form = StorylineForm()
    return render(request,'myapp/storyline_form.html',{'form':form})

@login_required
def add_member(request,uuid):
    story = get_object_or_404(Story, uuid=uuid)
    if request.user in story.members.all() or request.user == story.author:
        return HttpResponse('dont try this shit with me')
    else:
        request.user.userprofile.member_of.add(story)
        return redirect('myapp:story_detail',pk=story.pk)

@login_required
def addstory(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = User.objects.get(username=request.user.username)

            form.save()
            request.user.userprofile.member_of.add(story)
            return redirect('myapp:story_detail',pk=story.pk)
    else:
        form = StoryForm()
    return render(request, 'myapp/story_form.html', {'form':form})

@login_required
def event_complete_toggle(request,pk):
    event = get_object_or_404(StoryEvent,pk=pk)
    event.complete_toggle()
    return redirect('myapp:story_detail',pk=event.storyline.story.pk)

@login_required
def story_unstarr(request,pk):
    story = get_object_or_404(Story,pk=pk)
    request.user.userprofile.starred.remove(story)

    return redirect('myapp:story_list')

@login_required
def story_starr(request,pk):
    story = get_object_or_404(Story,pk=pk)
    request.user.userprofile.starred.add(story)

    return redirect('myapp:story_detail',pk=event.storyline.story.pk)


@login_required
def addeventcomment(request,pk):
    event = get_object_or_404(StoryEvent, pk=pk)
    if request.method == 'POST':
        form = EventCommentForm(request.POST)
        if form.is_valid():

            eventcomment = form.save(commit=False)
            eventcomment.author = User.objects.get(username=request.user.username)
            eventcomment.event = event

            form.save()
            return redirect('myapp:story_detail',pk=event.storyline.story.pk)
    else:
        form = EventCommentForm()
    return render(request,'myapp/eventcomment_form.html',{'form':form})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'myapp/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})
