from django.shortcuts import render
from .models import Book


def index(request):
    ctx = {}
    all_books = Book.objects.all()
    ctx['all_books'] = all_books
    return render(request, 'product/main.html', ctx)
