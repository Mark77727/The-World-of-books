from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance


# admin.site.register(Author)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')



admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)

#admin.site.register(BookInstance)

@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):pass

