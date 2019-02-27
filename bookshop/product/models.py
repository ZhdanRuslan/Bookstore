from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    isbn = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publish_date = models.DateField(editable=True, auto_created=True)

    def __str__(self):
        return f'title: {self.title} price: {self.price} ISBN: {self.isbn} date \
                {self.publish_date.strftime("%Y-%m-%d %H:%M:%S")}'


class WebRequest(models.Model):
    req = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.req} date {self.created.strftime("%Y-%m-%d %H:%M:%S")}'
