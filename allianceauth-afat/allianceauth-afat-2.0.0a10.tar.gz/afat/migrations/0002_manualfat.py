# Generated by Django 2.0.6 on 2018-06-26 01:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import afat.models


class Migration(migrations.Migration):

    dependencies = [
        ("eveonline", "0010_alliance_ticker"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("afat", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ManualAFat",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "character",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="eveonline.EveCharacter",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=models.SET(afat.models.get_sentinel_user),
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "afatlink",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="afat.AFatLink",
                    ),
                ),
            ],
        ),
    ]
