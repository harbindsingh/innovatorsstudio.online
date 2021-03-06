# Generated by Django 3.1.7 on 2021-05-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0013_event_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfullcourse',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='userCertificates/fullCourses/'),
        ),
        migrations.AddField(
            model_name='userminicourse',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='userCertificates/miniCourses/'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='class_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lecture_video',
            field=models.FileField(blank=True, null=True, upload_to='courseTutorials/'),
        ),
        migrations.AlterField(
            model_name='userfullcourse',
            name='phone_no',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userminicourse',
            name='phone_no',
            field=models.BigIntegerField(default=0),
        ),
    ]
