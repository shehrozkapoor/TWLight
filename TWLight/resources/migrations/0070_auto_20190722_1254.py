# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-22 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("resources", "0069_auto_20190530_1757")]

    operations = [
        migrations.AlterField(
            model_name="partner",
            name="account_length",
            field=models.DurationField(
                blank=True,
                help_text="The standard length of an access grant from this Partner. Entered as &ltdays hours:minutes:seconds&gt.",
                null=True,
            ),
        )
    ]
