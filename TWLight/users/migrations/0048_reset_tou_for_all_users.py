# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-14 16:15
from __future__ import unicode_literals

from django.db import migrations


def reset_tou(apps, schema_editor):
    # Uncheck terms_of_use boolean field and empty terms_of_use_date
    User = apps.get_model("users", "UserProfile")
    for user in User.objects.all():
        if user.terms_of_use:
            user.terms_of_use = False
            user.terms_of_use_date = None
            user.save()


class Migration(migrations.Migration):

    dependencies = [("users", "0047_auto_20191017_0459")]

    operations = [migrations.RunPython(reset_tou, elidable=True)]
