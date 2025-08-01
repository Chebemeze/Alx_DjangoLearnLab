from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length = 200)
  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length = 200)
  author = models.ForeignKey(Author, on_delete = models.CASCADE)

  def __str__(self):
    return f"Title: {self.title}, Author: {self.author}"

class Library(models.Model):
  name = models.CharField(max_length = 200)
  books = models.ManyToManyField(Book)

  def __str__(self):
    return f"Name: {self.name} books: {self.books}"

class Librarian(models.Model):
  name = models.CharField(max_length = 200)
  library = models.OneToOneField(Library, on_delete= models.CASCADE, related_name ='librarian')

  def __str__(self):
    return f"Name: {self.name} books: {self.library}"