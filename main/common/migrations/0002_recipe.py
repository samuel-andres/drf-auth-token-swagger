# Generated by Django 4.1 on 2022-08-14 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("time_minutes", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
