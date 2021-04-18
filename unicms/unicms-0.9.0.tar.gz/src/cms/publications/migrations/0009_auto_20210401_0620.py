# Generated by Django 3.1.6 on 2021-04-01 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmspublications', '0008_auto_20210308_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationattachment',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicationattachment_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicationattachment',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicationattachment_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicationblock',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicationblock_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicationblock',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicationblock_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicationgallery',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicationgallery_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicationgallery',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicationgallery_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicationlink',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicationlink_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicationlink',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicationlink_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicationrelated',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicationrelated_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicationrelated',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicationrelated_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
