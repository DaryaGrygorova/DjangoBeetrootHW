from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Note


def notes(request):
    notes_list = Note.objects.order_by('-create_at')
    return render(request, 'notes/notes.html', {'notes': notes_list})
