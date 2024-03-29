# Generated by Django 4.2.7 on 2023-12-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "title",
                    models.CharField(
                        choices=[
                            ("To do", "To do"),
                            ("Note", "Note"),
                            ("Event", "Event"),
                        ],
                        default="To do",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Note",
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
                ("title", models.CharField(blank=True, max_length=200, null=True)),
                ("text", models.TextField(blank=True, null=True)),
                ("reminder", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=models.SET("Todo"), to="notes.category"
                    ),
                ),
            ],
        ),
    ]
