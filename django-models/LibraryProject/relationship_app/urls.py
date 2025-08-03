from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
  path('listbook/', list_books, name='listbooks'),
  path('librarybooks/<int:pk>/', LibraryDetailView.as_view(), name='libbooks'),
]
