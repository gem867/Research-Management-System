# Generated by Django 5.1.3 on 2024-12-08 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rms_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='reader_department',
            new_name='author_department',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='reader_name',
            new_name='author_name',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='reader_type',
            new_name='author_type',
        ),
    ]
