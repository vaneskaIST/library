
from django.contrib import admin
from .models import Author, Book, Rental

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'available')

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('book', 'rental_date', 'return_date')
