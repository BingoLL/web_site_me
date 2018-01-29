# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_aboutme_aboutsite_comment_friendweb_messageboard'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name_plural': '关于作者', 'verbose_name': '关于作者', 'ordering': ('created_time',)},
        ),
        migrations.AlterModelOptions(
            name='aboutsite',
            options={'verbose_name_plural': '关于本站', 'verbose_name': '关于本站', 'ordering': ('created_time',)},
        ),
    ]
