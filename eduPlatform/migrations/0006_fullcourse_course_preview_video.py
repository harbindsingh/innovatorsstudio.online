# Generated by Django 3.1.7 on 2021-04-30 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0005_auto_20210430_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullcourse',
            name='course_preview_video',
            field=models.FileField(null=True, upload_to='course_preview_videos/'),
        ),
    ]
