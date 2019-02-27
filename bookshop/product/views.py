from django.shortcuts import render, get_object_or_404, redirect

from .forms import BookForm
from .models import Book, WebRequest


def index(request):
    WebRequest.objects.create(req = request)
    ctx = {}
    all_books = Book.objects.all()
    ctx['all_books'] = all_books

    return render(request, 'product/main.html', ctx)


def book_list(request, template_name='product/book_list.html'):
    WebRequest.objects.create(req=request)
    book = Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)


def book_view(request, pk, template_name='product/book_detail.html'):
    WebRequest.objects.create(req=request)
    book = get_object_or_404(Book, pk=pk)
    return render(request, template_name, {'object': book})


def book_create(request, template_name='product/book_form.html'):
    WebRequest.objects.create(req=request)
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form': form})


def book_update(request, pk, template_name='product/book_form.html'):
    WebRequest.objects.create(req=request)
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form': form})


def book_delete(request, pk, template_name='product/book_confirm_delete.html'):
    WebRequest.objects.create(req=request)
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, template_name, {'object': book})


def get_last_ten(request):
    ctx = {}
    last_ten = WebRequest.objects.filter().order_by('-id')[:10]
    ctx['last_ten'] = last_ten

    return render(request, 'product/last.html', ctx)
