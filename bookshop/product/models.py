import logging
from django.db import models
from django.db.models import signals

logger = logging.getLogger(__name__)
logging.basicConfig(filename='bookshop/product/logs/app_logs.log', level=logging.INFO)


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


def signal_callback(sender, **kwargs):
    if 'created' in kwargs.keys():
        if kwargs['created']:
            logger.info('Book was created')
        elif not kwargs['created']:
            logger.info('Book was edited')
    else:
        logger.info('Book was deleted')


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    isbn = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publish_date = models.DateField(editable=True, auto_created=True)

    def __str__(self):
        return f'title: {self.title} price: {self.price} ISBN: {self.isbn} date \
                {self.publish_date.strftime("%Y-%m-%d %H:%M:%S")}'


signals.post_save.connect(receiver=signal_callback, sender=Book)
signals.post_delete.connect(receiver=signal_callback, sender=Book)


class WebRequest(models.Model):
    req = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.req} date {self.created.strftime("%Y-%m-%d %H:%M:%S")}'
