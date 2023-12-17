import datetime
from pprint import pprint

from django.test import TestCase, RequestFactory
from django.urls import reverse

from .forms import NoteForm
from .models import Note, Category
from .views import NotesListView

TEST_NOTES_DATA = [{
        'category': 1,
        'title': 'title 1',
        'text': 'note description',
        'reminder': '2023-12-14'
    },
    {
        'category': 3,
        'title': 'title 2',
        'text': 'some text',
        'reminder': '2023-12-13'
    },
    {
        'category': 2,
        'title': 'title 3',
        'text': 'note description',
        'reminder': '2023-12-15'
    }
]

class NoteModelTest(TestCase):
    categories = {}
    notes = {}
    @classmethod
    def setUpTestData(cls):
        cls.categories = {
            1: Category.objects.create(category_id=1, title="To do"),
            2: Category.objects.create(category_id=2, title="Note"),
            3: Category.objects.create(category_id=3, title="Event")
        }
    def test_note_model_save_and_retrieve_data(self):
        for i, data_set in enumerate(TEST_NOTES_DATA):
            self.notes[i] = Note(
                category=NoteModelTest.categories[data_set['category']],
                title=data_set['title'],
                text=data_set['text'],
                reminder=data_set['reminder']
            )
            self.notes[i].save()

        all_notes = Note.objects.all()
        self.assertEqual(len(all_notes), 3)
        self.assertIsInstance(self.notes[0].category, Category)
        self.assertEqual(self.notes[0].title, 'title 1')
        self.assertEqual(self.notes[0].text, 'note description')
        self.assertEqual(self.notes[0].reminder, '2023-12-14')

        self.assertIsInstance(self.notes[1].category, Category)
        self.assertEqual(self.notes[1].title, 'title 2')
        self.assertEqual(self.notes[1].text, 'some text')
        self.assertEqual(self.notes[1].reminder, '2023-12-13')

        self.assertIsInstance(self.notes[2].category, Category)
        self.assertEqual(self.notes[2].title, 'title 3')
        self.assertEqual(self.notes[2].text, 'note description')
        self.assertEqual(self.notes[2].reminder, '2023-12-15')


class CreateNoteViewTestCase(TestCase):

    def test_view_save_and_retrieve_data(self):
        Category.objects.create(category_id=1, title="To do")
        note_content = {
            'category': 1,
            'title': 'title new',
            'text': 'note description',
            'reminder': '2023-12-14',
        }
        request = self.client.post('/notes/create/', data=note_content)
        self.assertRedirects(request, reverse('notes'))

        notes = Note.objects.all()
        self.assertEqual(len(notes), 1)

        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'title new')
        self.assertEqual(note.text, 'note description')
        self.assertEqual(note.reminder, datetime.date(2023, 12, 14))


class UpdateNoteViewTestCase(TestCase):
    def test_changes_are_saved(self):
        category = Category.objects.create(category_id=1, title="To do")
        note = Note.objects.create(
            category=category,
            title='title 3',
            text='some text',
            reminder='2023-12-15')

        changes = {
            'category': note.category_id,
            'title': 'title new',
            'text': 'note description',
            'reminder': note.reminder
        }

        request = self.client.post(reverse('update-note', args=[note.id]), data=changes)
        self.assertRedirects(request, reverse('notes'))

        note.refresh_from_db()
        self.assertEqual(note.category_id, 1)
        self.assertEqual(note.title, 'title new')
        self.assertEqual(note.text, 'note description')
        self.assertEqual(note.reminder,  datetime.date(2023, 12, 15))


class NotesListViewTestCase(TestCase):
    category = {}

    @classmethod
    def setUpTestData(cls):
        cls.category = {
            1: Category.objects.create(category_id=1, title="To do"),
            2: Category.objects.create(category_id=2, title="Note"),
            3: Category.objects.create(category_id=3, title="Event")
        }

        for data_set in TEST_NOTES_DATA:
            Note.objects.create(
                category=cls.category[data_set['category']],
                title=data_set['title'],
                text=data_set['text'],
                reminder=data_set['reminder']
            )

    def test_notes_page_displays_all_entries(self):
        response = self.client.get(reverse("notes"))
        html = response.content.decode("utf8")

        self.assertEqual(
            response.resolver_match.func.__name__,
            NotesListView.as_view().__name__
        )
        self.assertIn("title 1", html)
        self.assertIn("title 2", html)
        self.assertIn("title 3", html)

    def test_notes_page_sort_entries_by_date_correctly(self):
        response = self.client.get(reverse("notes")+"?sort=create_at")
        html = response.content.decode("utf8")
        self.assertTrue(html.find("title 1") < (html.find("title 2")))
        self.assertTrue(html.find("title 2") < (html.find("title 3")))

    def test_notes_page_sort_entries_by_category_correctly(self):
        response = self.client.get("/notes/?sort=category")
        html = response.content.decode("utf8")
        self.assertTrue(html.find("title 1") < html.find("title 3"))
        self.assertTrue(html.find("title 3") < html.find("title 2"))

    def test_notes_page_search_by_title_show_correct_entries(self):
        response = self.client.get("/notes/?search-area=1")
        html = response.content.decode("utf8")
        self.assertIn("title 1", html)
        self.assertNotIn("title 2", html)
        self.assertNotIn("title 3", html)
