# Generated by Django 3.1.6 on 2021-03-14 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmspublications', '0008_auto_20210308_1404'),
        ('cmspages', '0005_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagepublication',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmspages.page'),
        ),
        migrations.AlterField(
            model_name='pagepublication',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmspublications.publication'),
        ),
    ]
