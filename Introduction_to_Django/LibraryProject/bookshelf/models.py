from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField(default=2000)

  def __str__(self):
    return f"Book: {self.title} by {self.author} ({self.publication_year})"