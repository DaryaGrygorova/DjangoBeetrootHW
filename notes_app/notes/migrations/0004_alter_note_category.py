# Generated by Django 4.2.7 on 2023-12-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0003_alter_category_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="category",
            field=models.ForeignKey(on_delete=models.SET(2), to="notes.category"),
        ),
    ]
