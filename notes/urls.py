from django.urls import path
from .views import *

urlpatterns = [
    path('user-notes/',UserNotes.as_view()),
    path('edit-notes/<int:pk>',EditNotes.as_view()),
    path('append-note/<int:pk>',AppendNote.as_view())
]
