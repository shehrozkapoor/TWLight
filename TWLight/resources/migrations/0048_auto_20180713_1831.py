# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("resources", "0047_auto_20180703_1253")]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="description_ar",
            field=models.TextField(
                blank=True,
                help_text="Optional description of this partner's resources.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="partner",
            name="send_instructions_ar",
            field=models.TextField(
                blank=True,
                help_text="Optional instructions for sending application data to this partner.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="stream",
            name="description_ar",
            field=models.TextField(
                blank=True,
                help_text="Optional description of this stream's resources.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="textfieldtag",
            name="name_ar",
            field=models.TextField(max_length=100, null=True, verbose_name="Name"),
        ),
    ]
