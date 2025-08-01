from LibraryProject.relationship_app.models import Book
from LibraryProject.relationship_app.models import Library
from .models import Librarian
from .models import Author

author_name = "Benjamin Franklin"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
for e in books:
  print(e.title)


library_name = "Wheel of time"

# gets a single library object
# uses the forward relationship to then get all books associated with the library object 
library = Library.objects.get(name=library_name)
books = library.books.all()

# because of the one to one relationship, it gets the liberian associated with the library object
# with the help of a reverse attribute related_name = librarian
librarian = Librarian.objects.get(library=library)