# Generated by Django 4.1.2 on 2022-10-27 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0002_followrequest_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followrequest',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='followrequest',
            name='object',
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
        migrations.DeleteModel(
            name='FollowRequest',
        ),
    ]
