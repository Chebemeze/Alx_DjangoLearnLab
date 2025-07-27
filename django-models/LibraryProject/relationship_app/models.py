from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.Charfield(max_length = 200)

class Book(models.Model):
  title = models.Charfield(max_length = 200)
  author = models.foreignkey(Author, on_delete = models.CASCADE)

class Library(models.Model):
  name = models.Charfield(max_length = 200)
  books = models.ManyToManyField(Book, on_delete = models.CASCADE)

  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.Charfield(max_length = 200)
  library = models.OneToOneField(Library, on_delete= models.CASCADE)