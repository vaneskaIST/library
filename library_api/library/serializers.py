from rest_framework import serializers
from .models import Author, Book, Rental

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'birth_date']  # можно указать '__all__' для всех полей

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Это включит информацию об авторе

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'available']

class RentalSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Отображение имени пользователя
    book = BookSerializer(read_only=True)  # Отображение информации о книге

    class Meta:
        model = Rental
        fields = ['id', 'user', 'book', 'rental_date', 'return_date']
