# Generated by Django 3.1.7 on 2021-03-09 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_auto_20210305_1855"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="mail_updates",
        ),
    ]
