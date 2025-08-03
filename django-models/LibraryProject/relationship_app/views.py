from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views.generic import DetailView

# Create your views here.

def list(request):
  book = Book.objects.all()
  return render(request, 'relationship_app/list_books.html', {'book': book})

class LibraryDetailView(DetailView):
  # A class-based view for displaying details of a specific book.
  model = Library
  template_name = 'relationship_app/library_detail.html'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the book."""
    context = super().get_context_data(**kwargs)  # Get default context data
    library = self.get_object()  # Retrieve the current book instance
    context['book'] = library.books.all()
    return context