# Generated by Django 5.0 on 2023-12-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                    "img",
                    models.ImageField(upload_to="media", verbose_name="Blog Image"),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Blog Title")),
                ("describtion", models.TextField(verbose_name="Describtion")),
                ("post_date", models.DateField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Blog Post",
                "verbose_name_plural": "Blogs",
            },
        ),
    ]
