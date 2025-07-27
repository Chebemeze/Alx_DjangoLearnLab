from LibraryProject.relationship_app.models import Book
from LibraryProject.relationship_app.models import Library
from .models import Librarian

books = Book.objects.filter(author="author")
for e in books:
  print(e.title)

books = Library.objects.filter(books = books)

library = Library.objects.get(name = "name")
librarian = Librarian.objects.get(library = library)