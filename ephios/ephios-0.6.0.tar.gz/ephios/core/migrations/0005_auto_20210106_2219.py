# Generated by Django 3.1.4 on 2021-01-06 21:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_auto_20201014_1648"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="qualificationgrant",
            unique_together={("qualification", "user")},
        ),
        migrations.CreateModel(
            name="WorkingHours",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("hours", models.DecimalField(decimal_places=2, max_digits=7)),
                ("reason", models.CharField(blank=True, default="", max_length=1024)),
                ("datetime", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Consequence",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("slug", models.CharField(max_length=255)),
                ("data", models.JSONField(default=dict)),
                (
                    "state",
                    models.TextField(
                        choices=[
                            ("needs_confirmation", "needs confirmation"),
                            ("executed", "executed"),
                            ("failed", "failed"),
                            ("denied", "denied"),
                        ],
                        default="needs_confirmation",
                        max_length=31,
                    ),
                ),
                ("executed_at", models.DateTimeField(blank=True, null=True)),
                ("fail_reason", models.TextField(blank=True, max_length=255)),
                (
                    "decided_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="confirmed_consequences",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="confirmed by",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="affecting_consequences",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="affected user",
                    ),
                ),
            ],
        ),
    ]
