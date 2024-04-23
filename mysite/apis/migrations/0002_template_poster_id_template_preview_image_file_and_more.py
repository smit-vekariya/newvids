# Generated by Django 5.0 on 2024-04-23 06:09

import django.core.files.storage
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='poster_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.poster'),
        ),
        migrations.AddField(
            model_name='template',
            name='preview_image_file',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='poster_template/preview_image_file/'),
        ),
        migrations.AddField(
            model_name='template',
            name='zip_file',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='poster_template/zip_file/'),
        ),
    ]
