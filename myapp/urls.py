from django.urls import path
from . import views
app_name = 'myapp'
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
    path('<int:pk>',views.StoryDetailView.as_view(),name='story_detail'),
    path('add/<uuid>',views.add_member,name='add_member'),
    path('stories/',views.StoryListView.as_view(),name='story_list'),
    path('',views.IndexView.as_view(),name='index_view'),
    path('storyline/<int:pk>/addevent/',views.addevent,name='addevent'),
    path('event/<int:pk>/addcomment/',views.addeventcomment,name='addeventcomment'),
    path('stories/new', views.addstory, name='addstory'),
    path('story/<int:pk>/createstoryline/', views.addstoryline, name='addstoryline'),
    path('complete/<int:pk>', views.event_complete_toggle ,name='complete_toggle'),
    path('story/<int:pk>/unstarr',views.story_unstarr,name='story_unstarr'),
    path('story/<int:pk>/starr',views.story_starr,name='story_starr'),
    path('story/<int:pk>/delete',views.delete_story,name='story_delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
