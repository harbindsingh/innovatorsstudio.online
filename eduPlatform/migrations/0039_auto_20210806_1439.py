# Generated by Django 2.2.14 on 2021-08-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0038_blog_post_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
