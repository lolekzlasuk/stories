from django.contrib import admin
from .models import UserProfile,Story,Storyline,StoryEvent
# Register your models here.
admin.site.register(UserProfile)

admin.site.register(Story)
admin.site.register(Storyline)
admin.site.register(StoryEvent)
