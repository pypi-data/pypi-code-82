# Generated by Django 3.1.6 on 2021-04-15 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmstemplates', '0002_auto_20210119_1359'),
        ('cmspages', '0008_auto_20210401_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageblock',
            name='block',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='cmstemplates.templateblock'),
        ),
    ]
