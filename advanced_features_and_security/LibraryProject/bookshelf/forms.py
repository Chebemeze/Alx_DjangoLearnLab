from django import forms
from .models import Book, Library, Librarian, UserProfile, Mechanical_Texbook

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['title']

class MechanicalForm(forms.ModelForm):
  class Meta:
    model = Mechanical_Texbook
    fields = ['title']