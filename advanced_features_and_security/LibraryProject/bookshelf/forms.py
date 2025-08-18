from django import forms
from .models import Book, Library, Librarian, UserProfile

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['title']