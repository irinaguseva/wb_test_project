# Generated by Django 4.2 on 2025-01-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0002_rename_points_creator_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
