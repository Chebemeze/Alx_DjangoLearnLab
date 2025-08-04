from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('listbook/', list_books, name='listbooks'),
  path('librarybooks/<int:pk>/', LibraryDetailView.as_view(), name='libbooks'),
  path('login/', auth_views.LoginView.as_view(), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('register/', register, name='register'),
]
