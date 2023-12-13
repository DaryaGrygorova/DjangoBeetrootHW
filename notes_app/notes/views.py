from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

NOTES = [
    {
        'id': 1,
        'title': "Note 1",
        'description': "Do something"
    },
    {
        'id': 2,
        'title': "Note 2",
        'description': "Do another something"
    },
    {
        'id': 3,
        'title': "Note 3",
        'description': "Just Do It!"
    }
]

def notes(request):
    return render(request, 'notes/notes.html', {'notes': NOTES})
