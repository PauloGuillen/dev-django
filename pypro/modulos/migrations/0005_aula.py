# Generated by Django 4.2 on 2023-04-15 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("modulos", "0004_alter_modulo_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Aula",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("titulo", models.CharField(max_length=64)),
                ("slug", models.SlugField(unique=True)),
                (
                    "modulo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="modulos.modulo"
                    ),
                ),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
    ]
