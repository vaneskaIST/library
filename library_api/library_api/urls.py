from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('library.urls')),  # Маршруты API
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Страница логина
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Страница логаута
]


