# Generated by Django 4.2.7 on 2023-12-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0008_remove_category_id_category_category_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]