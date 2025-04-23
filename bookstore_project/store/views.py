from django.shortcuts import render

# Create your views here.
# store/views.py
from django.views import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request):
        return render(request, 'store/home.html')
    
# store/views.py
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import models


# store/views.py (below LoginView)

class RegisterView(View):
    def get(self, request):
        return render(request, 'store/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            return render(request, 'store/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'store/register.html', {'error': 'Username already taken'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

    

class LoginView(View):
    def get(self, request):
        return render(request, 'store/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        return render(request, 'store/login.html', {'error': 'Invalid credentials'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

class AdminDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_staff:
            return HttpResponseForbidden("Admins only.")
        books = Book.objects.all()
        return render(request, 'store/admin_dashboard.html', {'books': books})

class AddBookView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_staff:
            return HttpResponseForbidden("Admins only.")
        return render(request, 'store/book_form.html')

    def post(self, request):
        if not request.user.is_staff:
            return HttpResponseForbidden("Admins only.")
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        stock = request.POST['stock']
        description = request.POST['description']

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            stock=stock,
            description=description
        )
        return redirect('admin_dashboard')

class EditBookView(LoginRequiredMixin, View):
    def get(self, request, pk):
        if not request.user.is_staff:
            return HttpResponseForbidden("Admins only.")
        book = Book.objects.get(pk=pk)
        return render(request, 'store/book_form.html', {'book': book})

    def post(self, request, pk):
        if not request.user.is_staff:
            return HttpResponseForbidden("Admins only.")
        book = Book.objects.get(pk=pk)
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.stock = request.POST['stock']
        book.description = request.POST['description']
        book.save()
        return redirect('admin_dashboard')

class DeleteBookView(LoginRequiredMixin, View):
    def get(self, request, pk):
        if not request.user.is_staff:
            return HttpResponseForbidden("Admins only.")
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('admin_dashboard')

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()  # Retrieve all books
        return render(request, 'store/book_list.html', {'books': books})



class BookDetailView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'store/book_detail.html', {'book': book})


class AddToCartView(View):
    def post(self, request, pk):
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if str(pk) in cart:
            cart[str(pk)] += quantity
        else:
            cart[str(pk)] = quantity

        request.session['cart'] = cart
        return redirect('book-list')

class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        books = Book.objects.filter(pk__in=cart.keys())
        cart_items = []
        total = 0
        for book in books:
            quantity = cart[str(book.pk)]
            subtotal = quantity * book.price
            total += subtotal
            cart_items.append({
                'book': book,
                'quantity': quantity,
                'subtotal': subtotal
            })
        return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})


class RemoveFromCartView(View):
    def get(self, request, pk):
        cart = request.session.get('cart', {})
        if str(pk) in cart:
            del cart[str(pk)]
            request.session['cart'] = cart
        return redirect('view_cart')

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     stock = models.IntegerField(default=0)  # Default value of 0 for stock

# store/views.py (add this after CartView)

class RemoveFromCartView(View):
    def post(self, request, pk):
        quantity_to_remove = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if str(pk) in cart:
            cart[str(pk)] -= quantity_to_remove
            if cart[str(pk)] <= 0:
                del cart[str(pk)]

        request.session['cart'] = cart
        return redirect('cart')


# store/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'store/home.html'

