from django.shortcuts import render

from rest_framework import viewsets
from .models import Author, Book, Rental
from .serializers import AuthorSerializer, BookSerializer, RentalSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated, AllowAny
from .forms import BookForm
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]  # Разрешаем доступ без авторизации

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Разрешаем доступ без авторизации

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated]  # Требуем авторизацию


# Для отображения на сайте (интерфейс)
def index(request):
    return render(request, 'library/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'library/book_detail.html', {'book': book})

@login_required
def rent_book(request, id):
    book = get_object_or_404(Book, id=id)
    if book.available:
        Rental.objects.create(user=request.user, book=book)
        book.available = False
        book.save()
    return redirect('book_list')

@login_required
def rental_history(request):
    rentals = Rental.objects.filter(user=request.user)
    return render(request, 'library/rental_history.html', {'rentals': rentals})


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Перенаправление на страницу списка книг
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})