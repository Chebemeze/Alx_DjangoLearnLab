from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('listbook/', list_books, name='listbooks'),
  path('librarybooks/<int:pk>/', LibraryDetailView.as_view(), name='libbooks'),
  path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
  path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
  path('register/', views.register, name='register'),
  path('admin/', views.admin_view, name='admin_view'),
  path('librarian/', views.librarian_view, name='librarian_view'),
  path('member/', views.member_view, name='member_view'),
  path('book/add', views.add_book, name='add_book'),
  path('book/<int:pk>/edit', views.edit_book, name='edit_book'),
  path('book/<int:pk>/delete', views.delete_book, name='delete_book'),
]