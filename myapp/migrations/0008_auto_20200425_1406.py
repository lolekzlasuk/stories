# Generated by Django 2.2.3 on 2020-04-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200425_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default-profile.png', upload_to='profile_pics'),
        ),
    ]
