from django.shortcuts import render, get_object_or_404, redirect
import logging

from .forms import BookForm
from .models import Book, WebRequest

logger = logging.getLogger(__name__)


def index(request):
    WebRequest.objects.create(req=request)
    ctx = {}
    all_books = []
    if request.method == 'GET' and request.GET.get('asc_button') == 'ASC':
        all_books = Book.objects.filter().order_by('publish_date')
    if request.method == 'GET' and request.GET.get('desc_button') == 'DESC':
        all_books = Book.objects.filter().order_by('-publish_date')
    else:
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
    logger.info('Creatin a book.')
    WebRequest.objects.create(req=request)
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        logger.info('Book was created.')
        return redirect('book_list')
    logger.error('Something wrong')
    return render(request, template_name, {'form': form})


def book_update(request, pk, template_name='product/book_form.html'):
    logger.info('Editing book.')
    WebRequest.objects.create(req=request)
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        logger.info('Book was edited.')
        return redirect('book_list')
    logger.error('Something wrong')
    return render(request, template_name, {'form': form})


def book_delete(request, pk, template_name='product/book_confirm_delete.html'):
    logger.info('Deleting book.')
    WebRequest.objects.create(req=request)
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        logger.info('Book was deleted.')
        return redirect('book_list')
    logger.error('Something wrong')
    return render(request, template_name, {'object': book})


def get_last_ten(request):
    WebRequest.objects.create(req=request)
    ctx = {}
    last_ten = WebRequest.objects.filter().order_by('-id')[:10]
    ctx['last_ten'] = last_ten

    return render(request, 'product/last.html', ctx)
