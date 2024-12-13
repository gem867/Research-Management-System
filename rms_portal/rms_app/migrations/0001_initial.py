# Generated by Django 5.1.3 on 2024-12-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.CharField(max_length=200)),
                ('reader_name', models.CharField(max_length=100)),
                ('reader_type', models.CharField(max_length=100)),
                ('reader_department', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]