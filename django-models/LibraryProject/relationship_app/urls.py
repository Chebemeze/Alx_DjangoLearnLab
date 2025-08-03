from django.urls import path
from relationship_app import views

urlpatterns = [
  path('listbook/', views.list, name='listbooks'),
  path('librarybooks/<int:pk>/', views.LibraryDetailView.as_view(), name='libbooks'),
]
