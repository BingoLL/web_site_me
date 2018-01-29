# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='文章标题')),
                ('slug', models.SlugField(unique_for_date='publish', max_length=250)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='正文')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='published', max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], verbose_name='文章状态')),
                ('views', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='blog_posts')),
                ('category', models.ForeignKey(to='mysite.Category')),
                ('tags', models.ManyToManyField(to='mysite.Tag', blank=True)),
            ],
            options={
                'verbose_name_plural': '文章',
                'ordering': ('-publish',),
                'verbose_name': '文章',
            },
        ),
    ]
