# Generated by Django 4.1.2 on 2022-11-24 23:32

import api.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('type', models.CharField(default='comment', max_length=50)),
                ('comment', models.TextField()),
                ('contentType', models.CharField(max_length=1024)),
                ('published', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('id', models.CharField(default=api.models.generate_id, max_length=1024, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.JSONField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inbox_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('type', models.CharField(max_length=1024)),
                ('title', models.CharField(max_length=1024)),
                ('id', models.CharField(max_length=1024, primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=1024)),
                ('origin', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('contentType', models.CharField(blank=True, default='text/plain', max_length=1024, null=True)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('categories', models.CharField(max_length=1024)),
                ('count', models.IntegerField(default=0)),
                ('comments', models.CharField(blank=True, max_length=1024, null=True)),
                ('published', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('visibility', models.CharField(blank=True, default='PUBLIC', max_length=1024, null=True)),
                ('unlisted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('inbox', models.ManyToManyField(to='api.inbox')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_image', to='api.post', verbose_name='Post')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=1024)),
                ('summary', models.TextField()),
                ('type', models.CharField(max_length=1024)),
                ('object', models.CharField(max_length=1024)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_comment', to='api.comment', verbose_name='Comment')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_post', to='api.post', verbose_name='Post')),
            ],
        ),
        migrations.CreateModel(
            name='FollowRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(default='You have a follow request', max_length=1024)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor', to=settings.AUTH_USER_MODEL)),
                ('object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL, verbose_name='Followed')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Follower')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='api.post', verbose_name='Post'),
        ),
    ]
