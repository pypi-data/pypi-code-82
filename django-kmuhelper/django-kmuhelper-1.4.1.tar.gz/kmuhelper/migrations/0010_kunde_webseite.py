# Generated by Django 3.0.4 on 2020-05-31 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kmuhelper', '0009_kunde_notiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='kunde',
            name='webseite',
            field=models.URLField(blank=True, default='', verbose_name='Webseite'),
        ),
    ]
