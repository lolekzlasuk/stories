# Generated by Django 2.2.3 on 2020-04-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20200425_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='member_of',
            field=models.ManyToManyField(default='', related_name='member_of', to='myapp.Story'),
        ),
    ]
