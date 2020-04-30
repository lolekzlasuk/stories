from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,Story,Storyline,StoryEvent,EventComment,UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('profile_pic','name')



class StoryForm(forms.ModelForm):
    class Meta():
        model = Story
        fields = ['title','description','short']

        widgets = {
                'title':forms.TextInput(attrs={'class': 'titleinput'}),
                'description':forms.TextInput(attrs={'class': 'editable'})
        }


class StorylineForm(forms.ModelForm):

    class Meta():
        model = Storyline
        fields = ('title',)

        # widgets = {
        #         'author':forms.TextInput(attrs={'class': 'textinputclass'}),
        #         'text':forms.TextInput(attrs={'class': 'editable medium-editor-textarea'})
        #         }


class EventForm(forms.ModelForm):
    class Meta():
        model = StoryEvent
        fields = ('title','text')

class EventCommentForm(forms.ModelForm):
    class Meta():
        model = EventComment
        fields = ('text',)
