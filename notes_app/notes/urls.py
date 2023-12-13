from django.urls import path, include

from .views import notes

urlpatterns = [
    path("", notes, name='notes'),
]
