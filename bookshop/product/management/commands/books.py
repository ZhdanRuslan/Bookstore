from django.core.management.base import BaseCommand

from ...models import Book


class Command(BaseCommand):
    help = 'Displays current time'

    def add_arguments(self, parser):
        parser.add_argument('sort_by', type=str, help='Order by ASC/DESC')

    def handle(self, *args, **kwargs):
        if kwargs['sort_by'].lower() == 'desc':
            books = Book.objects.all().order_by('-publish_date')
            for i in books:
                print(i)
        elif kwargs['sort_by'].lower() == 'asc':
            books = Book.objects.all().order_by('publish_date')
            for i in books:
                print(i)
