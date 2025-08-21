from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile, CustomUser, Mechanical_Texbook
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# admin.ModelAdmin
# class CustomUserAdmin(UserAdmin):
#   list_display = ('username', 'email', 'password', 'date_of_birth', 'profile_photo')
#   search_fields = ('username', 'date_of_birth')
#   list_filter = ('username', 'date_of_birth')

# class CustomUserAdmin(UserAdmin):
#   # Tell Django which fields to display
#   # Adds fields such as date_of_birth and profile_photo when
#   # when editing a user
#   fieldsets = UserAdmin.fieldsets + (
#     (None, {'fields': ('date_of_birth', 'profile_photo')}),
#   )
#   # Adds fields such as date_of_birth and profile_photo when
#   # when creating a new user
#   add_fieldsets = UserAdmin.add_fieldsets + (
#     (None, {'fields': ('date_of_birth', 'profile_photo')}),
#   )

class CustomUserAdmin(admin.ModelAdmin):
  def has_view_permission(self, request, obj=None):
    return (request.user.has_perm("bookshelf.can_view") or super().has_view_permission(request, obj))

  def has_add_permission(self, request):
    return (request.user.has_perm("bookshelf.can_create") or super().has_add_permission(request))

  def has_change_permission(self, request, obj=None):
    return (request.user.has_perm("bookshelf.can_edit") or super().has_change_permission(request, obj))

  def has_delete_permission(self, request, obj=None):
    return (request.user.has_perm("bookshelf.can_delete") or super().has_delete_permission(request, obj))


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
admin.site.register(Mechanical_Texbook)