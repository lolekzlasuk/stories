from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,Story,Storyline,StoryEvent,EventComment


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
        labels = {
            'username': ('Login'),
        }
        widgets = {
        'username':forms.TextInput(attrs={"class":"yolko"}),
        'email':forms.TextInput(attrs={"class":"yolko"}),
        'password':forms.TextInput(attrs={"class":"yolko"}),

        }
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('name','profile_pic',)
        widgets = {
                'name':forms.TextInput(attrs={"class":"yolko",}),

                }
        labels = {
            'name': ('Handle'),

        }

class StoryForm(forms.ModelForm):
    class Meta():
        model = Story
        fields = ['title','description',]

        widgets = {
                'title':forms.TextInput(attrs={'class': 'yolko',"placeholder":"Title"}),
                'description':forms.Textarea(attrs={'rows':3,'cols':30,'class': ' yolko',"placeholder":"Description(optional)"})
        }
        labels = {
            'title':(''),
            'description':('')
        }

class StorylineForm(forms.ModelForm):

    class Meta():
        model = Storyline
        fields = ('title',)
        widgets = {
                'title':forms.TextInput(attrs={'class': ' yolko',"placeholder":"Title"})
                }
        labels = {
            'title':(''),
        }

class EventForm(forms.ModelForm):
    class Meta():
        model = StoryEvent
        fields = ('title','text')

        widgets = {
                        'title':forms.TextInput(attrs={'class': ' yolko',"placeholder":"Title"}),
                        'text':forms.Textarea(attrs={"rows":2,'class': ' yolko',"placeholder":"Description(optional)"})
                        }
        labels = {
            'text': (''),
            'title':('')
        }

class EventCommentForm(forms.ModelForm):
    class Meta():
        model = EventComment
        fields = ('text',)
        widgets = {
                'text':forms.Textarea(attrs={"rows":2,"placeholder":" Add a comment...","class":"comment-input"})
                }
        labels = {
            'text': (''),
        }
