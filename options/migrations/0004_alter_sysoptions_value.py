# Generated by Django 3.2.9 on 2023-12-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0003_migrate_languages_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sysoptions',
            name='value',
            field=models.JSONField(),
        ),
    ]