from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

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
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'userprofile')

# setting up automatic UserProfile creation making use of django signals
# It creates the Userprofile for the User and then saves the profile using save_UserProfile to database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_UserProfile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_UserProfile(sender, instance, **kwargs):
  instance.userprofile.save()

# custom manager for customUser
class CustomUserManager(BaseUserManager):
  def create_user(self, username, email, password, **extra_fields):
    if not email:
      raise ValueError("Please provide an email")
    if not password:
      raise ValueError("Please provide a valid password")

    if not extra_fields.get('is_superuser', False):
      # extra_fields.get('is_superusr', False) checks if it a superuser
      # if no value is given it fives it False. if not False passes the if
      # statement and moves to the nested if statement to check the
      # date of birth and profile photo
      if not extra_fields.get('date_of_birth'):
        raise ValueError(f"Please provide date of birth before proceeding")
      if not extra_fields.get('profile_photo'):
        raise ValueError(f"Please provide a profile photo before proceeding")
    # The above codes enforces the provision of date_of_birth and
    # profile_photo for normal users

    email= self.normalize_email(email)
    # converts email to lowercase
    user = self.model(username=username, email= email, **extra_fields)
    # creates an object called user from the cusromUser model
    user.set_password(password)  
    # ensures that a hashed password is stored
    user.save(using=self._db)
    # saves the object to the right database
    return user
    # return the user object

  def create_superuser(self, username, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError("Superuser must have is_staff=True.")
    if extra_fields.get('is_superuser') is not True:
      raise ValueError("Superuser must have is_superuser=True.")

    return self.create_user(username, email, password, **extra_fields)

# Implementing custom User model extending the fields of
# djangos default User model. in this case we have two extra fields
# date_of_birth and profile_photo
class CustomUser(AbstractUser):
  date_of_birth = models.DateField(null = True, blank = True)
  profile_photo = models.ImageField(null = True, blank = True)

  objects = CustomUserManager()
  # links customUserManager to customerUser model. customUserManager manages customerUser.

# Creating a new model called Mechanical Textbooks to test permission and Groups on
class Mechanical_Textbook(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete = models.CASCADE)

  class Meta:
    permissions = [
      ("can_view", "can view mechanical books"),
      ("can_create", "can create mechanical books"),
      ("can_edit", "can edit mechanical books"),
      ("can_delete", "can delete mechanical books"),
    ]