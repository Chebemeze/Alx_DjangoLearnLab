from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('listbook/', list_books, name='listbooks'),
  path('librarybooks/<int:pk>/', LibraryDetailView.as_view(), name='libbooks'),
  path('login/', LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
  path('logout/', LogoutView.as_view(template_name='bookshelf/logout.html'), name='logout'),
  path('register/', views.register, name='register'),
  path('admin/', views.admin_view, name='admin_view'),
  path('librarian/', views.librarian_view, name='librarian_view'),
  path('member/', views.member_view, name='member_view'),
  path('add_book/', views.add_book, name='add_book'),
  path('<int:pk>/edit_book/', views.edit_book, name='edit_book'),
  path('<int:pk>/delete_book', views.delete_book, name='delete_book'),


  path('list_mechbook/', views.list_mechbook, name='list_mechbook'),
  path('create_mechbook/', views.create_mechbook, name='create_mechbook'),
  path('view_mechbook/', views.view_mechbook, name='view_mechbook'),
  path('<int:pk>/edit_mechbook/', views.edit_mechbook, name='edit_mechbook'),
  path('<int:pk>/delete_mechbook/', views.delete_mechbook, name='delete_mechbook'),
]