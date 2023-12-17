from datetime import date

from django.db import models


CATEGORY_CHOICES = [
    ("1", "To do"),
    ("2", "Note"),
    ("3", "Event")
]


class Category(models.Model):
    """Model for note categories"""
    category_id = models.IntegerField(unique=True, primary_key=True, null=False, blank=False, serialize=True)
    title = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.title


class Note(models.Model):
    """Model for notes"""
    category = models.ForeignKey(Category, on_delete=models.SET('Todo'), null=False, blank=False, serialize=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    reminder = models.DateField(default=date.today)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
