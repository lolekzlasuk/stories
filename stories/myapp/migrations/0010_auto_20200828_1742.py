# Generated by Django 2.1.15 on 2020-08-28 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_userprofile_member_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcomment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.StoryEvent'),
        ),
        migrations.AlterField(
            model_name='story',
            name='description',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='story',
            name='short',
            field=models.TextField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='storyevent',
            name='storyline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='myapp.Storyline'),
        ),
        migrations.AlterField(
            model_name='storyevent',
            name='text',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='storyline',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storylines', to='myapp.Story'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
