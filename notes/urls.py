from django.urls import path
from .views import *

urlpatterns = [
    path('user-notes/',UserNotes.as_view()),
    path('edit-notes/<int:pk>',EditNotes.as_view()),
]
