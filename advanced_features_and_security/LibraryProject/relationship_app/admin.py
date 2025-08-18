from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile, CustomUser

# Register your models here.


class ModelAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'password', 'date_of_birth', 'profile_photo')
  search_fields = ('username', 'date_of_birth')
  list_filter = ('username', 'date_of_birth')

admin.site.register(CustomUser, ModelAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)