# Generated by Django 3.2.9 on 2024-05-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20240506_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='student_id',
            field=models.TextField(null=True),
        ),
    ]