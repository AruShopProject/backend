# Generated by Django 4.2.9 on 2024-01-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slider",
            name="time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
