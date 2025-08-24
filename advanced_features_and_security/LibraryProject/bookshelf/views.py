from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Mechanical_Textbook
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .forms import BookForm, MechanicalForm
from .forms import ExampleForm



# Create your views here.

def list_books(request):
  book = Book.objects.all()
  return render(request, 'bookshelf/list_books.html', {'book': book})

class LibraryDetailView(DetailView):
  # A class-based view for displaying details of a specific book.
  model = Library
  template_name = 'bookshelf/library_detail.html'

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
  return render(request, 'bookshelf/register.html', context)

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
  return render(request, 'bookshelf/admin_view.html')

@user_passes_test(Librarian_func)
def librarian_view(request):
  return render(request, 'bookshelf/librarian_view.html')

@user_passes_test(Member_func)
def member_view(request):
  return render(request, 'bookshelf/member_view.html')

# creating views to check the permission of a user before
# granting them various access to add, update and delete book

# ADD a Book
@permission_required ('bookshelf.can_add_book', raise_exception= False)
# raise_exception = False will enable user to be redirected to the login page
#  if the user doesn't have permission whether or not they are logged in
def add_book(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('list_books')

# else creates a case where POST == GET and an empty form is created
  else:
    form = BookForm()
  return render(request, 'bookshelf/book_form.html', {'form': form})


# Edit an existing book
@permission_required('bookshelf.can_change_book', raise_exception= False)
def edit_book(request, pk):
  book = get_object_or_404(Book, pk = pk)
  # gets a book using its ID
  if request.method == 'POST':
    form = BookForm(request.POST, instance = book)
    # instance = book used here ensures that a particular 'book'
    # is edited instead of creating a new one
    if form.is_valid():
      form.save()
      return redirect('list_book')
  else:
    form = BookForm(instance = book)
  return render(request, 'bookshelf/book_form.html', {'form': form})


# Delete a Book
@permission_required ('bookshelf.can_delete_book', raise_exception = False)
def delete_book(request, pk):
  book = get_object_or_404(Book, pk=pk)
  if request.method == 'POST':
    book.delete()
    return redirect('list_book')
  return render(request, 'bookshelf/confirm_delete.html', {'book':book})
# the last return used automatically handles GET request and
# direct it back to the delete_book() to delete the book because now
# request.method == 'POST'


# The below decorators and methods will handle the view of
# Mechanical_Textbooks for group such as Editors, viewers, and Admins
# Creates a Mechanical book
@permission_required('bookshelf.can_create', raise_exception= True)
# raise_exception = True will display error 403
#  if the user doesn't have permission
def create_mechbook(request):
  if request.method == 'POST':
    form = ExampleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('book_list')

# else creates a case where POST == GET and an empty form is created
  else:
    form = ExampleForm()
  return render(request, 'bookshelf/form_example.html', {'form': form})

def book_list(request):
  book = Mechanical_Textbook.objects.all()
  return render(request, 'bookshelf/book_list.html', {'book':book})
# View mechanical books
@permission_required('bookshelf.can_view', raise_exception= True)
def view_mechbook(request):
  return redirect('book_list')

# Edit an existing Mechanical book
@permission_required('bookshelf.can_edit', raise_exception= True)
def edit_mechbook(request, pk):
  book = get_object_or_404(Mechanical_Textbook, pk = pk)
  # gets a book using its ID
  if request.method == 'POST':
    form = ExampleForm(request.POST, instance = book)
    # instance = book used here ensures that a particular 'book'
    # is edited instead of creating a new one
    if form.is_valid():
      form.save()
      return redirect('book_list')
  else:
    form = ExampleForm(instance = book)
  return render(request, 'bookshelf/form_example.html', {'form': form})


# Delete a Mechanical book
@permission_required ('bookshelf.can_delete', raise_exception = True)
def delete_mechbook(request, pk):
  book = get_object_or_404(Mechanical_Textbook, pk=pk)
  if request.method == 'POST':
    book.delete()
    return redirect('book_list')
  return render(request, 'bookshelf/confirm_delete.html', {'book':book})