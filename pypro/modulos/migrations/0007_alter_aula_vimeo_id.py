# Generated by Django 4.2 on 2023-04-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modulos", "0006_aula_vimeo_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aula",
            name="vimeo_id",
            field=models.CharField(max_length=32),
        ),
    ]
