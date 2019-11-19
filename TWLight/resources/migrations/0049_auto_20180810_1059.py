# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-10 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("resources", "0048_auto_20180713_1831")]

    operations = [
        migrations.AlterField(
            model_name="partner",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Available"), (1, "Not available"), (2, "Waitlisted")],
                default=1,
                help_text="Should this Partner be displayed to users? Is it open for applications right now?",
            ),
        )
    ]
