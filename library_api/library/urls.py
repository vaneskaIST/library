from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, RentalViewSet, index, book_list, book_detail, rent_book, rental_history, add_book
from django.urls import path

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)  # Роут для авторов
router.register(r'books', BookViewSet)      # Роут для книг
router.register(r'rentals', RentalViewSet)  # Роут для аренд

# Маршруты для пользовательского интерфейса
urlpatterns = [
    path('', index, name='index'),
    path('books/', book_list, name='book_list'),
    path('book/<int:id>/', book_detail, name='book_detail'),
    path('book/<int:id>/rent/', rent_book, name='rent_book'),
    path('rentals/', rental_history, name='rental_history'),
    path('add_book/', add_book, name='add_book'),
]

# Добавляем маршруты API
urlpatterns += router.urls
