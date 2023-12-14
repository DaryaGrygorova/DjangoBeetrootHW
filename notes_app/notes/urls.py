from django.urls import path
from .views import NotesListView, CreateNoteView, UpdateNoteView, DeleteNoteView, NoteDetails

urlpatterns = [
    path("", NotesListView.as_view(), name='notes'),
    path("note/<int:pk>/", NoteDetails.as_view(), name='note-details'),
    path("create/", CreateNoteView.as_view(), name='create-note'),
    path("update/<int:pk>/", UpdateNoteView.as_view(), name='update-note'),
    path("delete/<int:pk>/", DeleteNoteView.as_view(), name='delete-note'),
]
