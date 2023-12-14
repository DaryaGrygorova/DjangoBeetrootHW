from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Note
from .forms import NoteForm


class NotesListView(ListView):
    model = Note
    template_name = 'notes/notes.html'
    context_object_name = "notes"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # filter data by search query
        search_input = self.request.GET.get("search-area", '')
        if search_input != "":
            context["notes"] = context["notes"].filter(title__icontains=search_input)
        context["search_input"] = search_input

        # ordering data by creation date
        sort_by = self.request.GET.get("sort", '')
        if sort_by != "":
            context["notes"] = context["notes"].order_by(sort_by)

        return context


class NoteDetails(DeleteView):
    model = Note
    template_name = 'notes/note-details.html'
    context_object_name = "note"


class CreateNoteView(CreateView):
    model = Note
    template_name = 'notes/note-form.html'
    form_class = NoteForm
    success_url = reverse_lazy('notes')


class UpdateNoteView(UpdateView):
    model = Note
    template_name = 'notes/note-form.html'
    form_class = NoteForm
    success_url = reverse_lazy('notes')


class DeleteNoteView(DeleteView):
    model = Note
    template_name = 'notes/note-delete.html'
    success_url = reverse_lazy('notes')
