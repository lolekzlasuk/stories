from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import uuid
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',default='profile_pics/default-profile.png',blank=True)
    name = models.TextField(max_length=200, default='')
    starred = models.ManyToManyField('myapp.Story')
    member_of = models.ManyToManyField('Story',related_name='member_of',default='')
    def __str__(self):
        return self.user.username

class Story(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    title = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    description =  models.TextField(max_length=500,default='')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=False)
    members = models.ManyToManyField('auth.User',related_name='member')
    def get_absolute_url(self):
        return reverse('story_detail',kwargs={'pk':self.pk,'uuid':self.uuid})
    short = models.TextField(max_length=8,default='')

    def __str__(self):
        return self.title

class Storyline(models.Model):
    story = models.ForeignKey('myapp.Story',related_name='storylines',on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1000)
    title = models.TextField(max_length=200)

    def get_absolute_url(self):
        return reverse('storyline_list')

    def __str__(self):
        return self.title

class StoryEvent(models.Model):
    storyline = models.ForeignKey('myapp.Storyline',related_name='events',on_delete=models.CASCADE)
    title = models.TextField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    created_date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)

    text = models.TextField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def complete_toggle(self):
        if self.completed == True:
            self.completed = False
        else:
            self.completed = True
            self.completed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class membership(models.Model):
    story = models.ManyToManyField('myapp.Story')
    user = models.ManyToManyField('auth.user')

class EventComment(models.Model):
    event = models.ForeignKey('myapp.StoryEvent',related_name='comments',on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField(max_length=200)
    title = models.TextField(max_length=200)

    def __str__(self):
        return self.title
