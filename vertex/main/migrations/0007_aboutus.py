# Generated by Django 5.0 on 2023-12-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_homebg"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutUs",
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
                ("t1", models.TextField()),
                ("t2", models.TextField()),
                ("t3", models.TextField()),
            ],
        ),
    ]