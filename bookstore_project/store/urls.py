# store/urls.py
from django.urls import path
from .views import HomeView
from .views import RegisterView, LoginView, LogoutView
from .views import BookListView
from django.urls import path
from .views import  BookListView, BookDetailView, AddToCartView, CartView, LoginView, LogoutView




urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
from .views import (
    AdminDashboardView, AddBookView, EditBookView, DeleteBookView
)

urlpatterns += [
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/book/add/', AddBookView.as_view(), name='add_book'),
    path('admin/book/<int:pk>/edit/', EditBookView.as_view(), name='edit_book'),
    path('admin/book/<int:pk>/delete/', DeleteBookView.as_view(), name='delete_book'),
]

# store/urls.py (append these)
from .views import (
    BookListView, BookDetailView, AddToCartView, CartView, RemoveFromCartView
)

urlpatterns += [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('cart/add/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='view_cart'),
    path('cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]

urlpatterns += [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# store/urls.py

from .views import RemoveFromCartView

urlpatterns += [
    path('remove-from-cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]

from django.urls import path
from .views import BookListView, BookDetailView, AddToCartView, CartView

urlpatterns += [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', CartView.as_view(), name='cart-view'),  # <-- required for 'View Cart'
]

from django.urls import path
from store.views import HomePageView  # Assuming you have this view

urlpatterns += [
    path('', HomePageView.as_view(), name='home'),  # Homepage URL
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', CartView.as_view(), name='cart-view'),
]
