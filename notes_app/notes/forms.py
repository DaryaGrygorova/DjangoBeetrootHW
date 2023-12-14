from django.forms import ModelForm, Textarea, TextInput

from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
