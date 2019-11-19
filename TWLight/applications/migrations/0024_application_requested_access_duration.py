# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-26 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("applications", "0023_auto_20190329_1631")]

    operations = [
        migrations.AddField(
            model_name="application",
            name="requested_access_duration",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (12, "12 months"),
                    (6, "6 months"),
                    (3, "3 months"),
                    (1, "1 month"),
                ],
                help_text="User selection of when they'd like their account to expire (in months). Only relevant if the applied partner/collection has authorization_method as 'proxy'.",
                null=True,
            ),
        )
    ]
