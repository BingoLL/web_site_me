# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='关于作者正文')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutSite',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='关于本站正文')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('reader_name', models.CharField(max_length=80, verbose_name='读者名字', null=True)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(related_name='comments', to='mysite.Post')),
            ],
            options={
                'verbose_name_plural': '评论',
                'verbose_name': '评论',
                'ordering': ('created_time',),
            },
        ),
        migrations.CreateModel(
            name='FriendWeb',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('logo_pic', models.ImageField(help_text='请上传40*120像素logo', upload_to='photos/friend_log/%Y/%m/%d/', verbose_name='友情链接logo图片')),
                ('friend_web_name', models.CharField(max_length=80, verbose_name='网站名字')),
                ('web_address', models.CharField(max_length=100, verbose_name='网址')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': '友情链接',
                'verbose_name': '友情链接',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=80, verbose_name='昵称', null=True)),
                ('body', models.TextField(verbose_name='欢迎留言')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': '留言',
                'verbose_name': '留言',
                'ordering': ('-created',),
            },
        ),
    ]
