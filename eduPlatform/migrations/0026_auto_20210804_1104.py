# Generated by Django 2.2.14 on 2021-08-04 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0025_auto_20210804_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='add',
        ),
        migrations.AddField(
            model_name='blogs',
            name='add_one_block',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogs',
            name='desc2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='img2',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
