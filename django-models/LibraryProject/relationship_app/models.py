from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import user_passes_test

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length = 200)
  def __str__(self):
    return self.name

# A Book table
class Book(models.Model):
  title = models.CharField(max_length = 200)
  author = models.ForeignKey(Author, on_delete = models.CASCADE)

# Modifying the Book model by introducing a Meta class to set permissions
# for different users
  class Meta:
    permissions = [
      ("can_add_book", "can add book"),
      ("can_change_book", "can change book"),
      ("can_delete_book", "can delete book"),
    ]

  def __str__(self):
    return f"Title: {self.title}, Author: {self.author}"

# A Library table
class Library(models.Model):
  name = models.CharField(max_length = 200)
  books = models.ManyToManyField(Book)

  def __str__(self):
    return f"Name: {self.name} books: {self.books}"

# A Librarian table
class Librarian(models.Model):
  name = models.CharField(max_length = 200)
  library = models.OneToOneField(Library, on_delete= models.CASCADE, related_name ='librarian')

  def __str__(self):
    return f"Name: {self.name} books: {self.library}"

# A UserProfile table
class UserProfile(models.Model):
  ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
  ]
  role = models.CharField(max_length = 100, choices = ROLE_CHOICES)
  user = models.OneToOneField(User, on_delete= models.CASCADE, related_name = 'userprofile')

# setting up automatic UserProfile creation making use of django signals
# It creates the Userprofile for the User and then saves the profile using save_UserProfile to database
@receiver(post_save, sender=User)
def create_UserProfile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_UserProfile(sender, instance, **kwargs):
  instance.user.save()