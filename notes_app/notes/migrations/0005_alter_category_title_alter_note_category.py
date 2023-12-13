# Generated by Django 4.2.7 on 2023-12-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0004_alter_note_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(
                choices=[("1", "To do"), ("2", "Note"), ("3", "Event")],
                default="To do",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="note",
            name="category",
            field=models.ForeignKey(on_delete=models.SET("Todo"), to="notes.category"),
        ),
    ]
