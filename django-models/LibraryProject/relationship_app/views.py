from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def list_books(request):
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

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = UserCreationForm()
  context = {'form':form}
  return render(request, 'relationship_app/register.html', context)

# Setting up role based views based on UserProfile roles
def Admin_func(user):
  return user.is_authenticated and getattr(user.userprofile, 'role', None) == 'Admin'

def Librarian_func(user):
  return user.is_authenticated and getattr(user.userprofile, 'role', None) == 'Librarian'

def Member_func(user):
  return user.is_authenticated and getattr(user.userprofile, 'role', None) == 'Member'

# @user_passes_test calls the various function to check if the user is logged
# and if the user has the necessary role before rendering to the that necessary role.
@user_passes_test(Admin_func)
def admin_view(request):
  return render(request, 'relationship_app/admin_view.html')

@user_passes_test(Librarian_func)
def librarian_view(request):
  return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(Member_func)
def member_view(request):
  return render(request, 'relationship_app/member_view.html')