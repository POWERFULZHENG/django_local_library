from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language
from .models import AuthorAdmin
# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
