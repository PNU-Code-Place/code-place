# Generated by Django 3.2.9 on 2024-02-08 08:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problem', '0023_alter_problem_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='solved_by',
            field=models.ManyToManyField(blank=True, related_name='problem_solved_by', to=settings.AUTH_USER_MODEL),
        ),
    ]