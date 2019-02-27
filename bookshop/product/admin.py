from django.contrib import admin
from .models import Author, Book, WebRequest

# register models in admin panel
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(WebRequest)
