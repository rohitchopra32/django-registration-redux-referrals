# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_refer_refercodes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refer',
            old_name='refered',
            new_name='referred',
        ),
        migrations.RenameField(
            model_name='refer',
            old_name='referer',
            new_name='referrer',
        ),
    ]
