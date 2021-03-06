from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import BookForm
from .models import Book, WebRequest


class Index(View):
    template_name = 'product/main.html'
    ctx = {}

    def get(self, request):
        if request.GET.get('asc_button') == 'ASC':
            all_books = Book.objects.filter().order_by('publish_date')
        elif request.GET.get('desc_button') == 'DESC':
            all_books = Book.objects.filter().order_by('-publish_date')
        else:
            all_books = Book.objects.all()
        self.ctx['all_books'] = all_books

        return render(request, self.template_name, self.ctx)


class BookList(View):
    template_name = 'product/book_list.html'
    ctx = {}

    def get(self, request):
        book = Book.objects.all()
        self.ctx['object_list'] = book
        return render(request, self.template_name, self.ctx)


class BookView(View):
    template_name = 'product/book_detail.html'
    ctx = {}

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        self.ctx['object'] = book
        return render(request, self.template_name, self.ctx)


class BookCreate(View):
    template_name = 'product/book_form.html'
    ctx = {}

    def get(self, request):
        form = BookForm(request.POST or None)
        self.ctx['form'] = form
        return render(request, self.template_name, self.ctx)

    def post(self, request):
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('book_list')


class BookUpdate(View):
    template_name = 'product/book_form.html'
    ctx = {}

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST or None, instance=book)
        self.ctx['form'] = form
        return render(request, self.template_name, self.ctx)

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST or None, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')


class BookDelete(View):
    template_name = 'product/book_confirm_delete.html'
    ctx = {}

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        self.ctx['object'] = book
        return render(request, self.template_name, self.ctx)

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if request.method == 'POST':
            book.delete()
            return redirect('book_list')


class LastRequests(View):
    template_name = 'product/last.html'
    ctx = {}

    def get(self, request):
        last_ten = WebRequest.objects.filter().order_by('-id')[:10]
        self.ctx['last_ten'] = last_ten
        return render(request, self.template_name, self.ctx)
