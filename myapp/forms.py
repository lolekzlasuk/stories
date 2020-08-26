from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,Story,Storyline,StoryEvent,EventComment,UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
        labels = {
            'username': ('Login'),
        }

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('name','profile_pic',)
        widgets = {
                'name':forms.TextInput(attrs={"class":""})
                }
        labels = {
            'name': ('Handle'),

        }

class StoryForm(forms.ModelForm):
    class Meta():
        model = Story
        fields = ['title','description',]

        widgets = {
                'title':forms.TextInput(attrs={'class': 'titleinput'}),
                'description':forms.TextInput(attrs={'class': 'editable'})
        }


class StorylineForm(forms.ModelForm):

    class Meta():
        model = Storyline
        fields = ('title',)
        widgets = {
                'title':forms.TextInput(attrs={"rows":2,})
                }
        # widgets = {
        #         'author':forms.TextInput(attrs={'class': 'textinputclass'}),
        #         'text':forms.TextInput(attrs={'class': 'editable medium-editor-textarea'})
        #         }


class EventForm(forms.ModelForm):
    class Meta():
        model = StoryEvent
        fields = ('title','text')

        widgets = {
                        'title':forms.TextInput(attrs={}),
                        'text':forms.Textarea(attrs={"rows":2})
                        }
        labels = {
            'text': ('Description'),
        }

class EventCommentForm(forms.ModelForm):
    class Meta():
        model = EventComment
        fields = ('text',)
        widgets = {
                'text':forms.Textarea(attrs={"rows":2,"cols":25,"placeholder":" Add a comment...","class":"comment-input"})
                }
        labels = {
            'text': (''),
        }
