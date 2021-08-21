# Generated by Django 2.2.14 on 2021-08-18 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eduPlatform', '0043_personaldevelopmentcourserating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldevelopmentcourserating',
            name='mini_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduPlatform.PersonalDevelopmentCourse'),
        ),
        migrations.CreateModel(
            name='UserPersonalDevelopmentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('phone_no', models.BigIntegerField(default=0)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='userCertificates/miniCourses/')),
                ('mini_course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eduPlatform.MiniCourse')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]