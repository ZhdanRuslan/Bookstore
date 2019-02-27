from django.urls import path

from .views import index, book_view, book_create, book_update, book_delete, book_list

urlpatterns = [
    path('', index),
    path('books', book_list, name='book_list'),
    path('view/<int:pk>', book_view, name='book_view'),
    path('new', book_create, name='book_new'),
    path('edit/<int:pk>', book_update, name='book_edit'),
    path('delete/<int:pk>', book_delete, name='book_delete'),
]
