from django.urls import path

from .views import Index, BookView, BookCreate, BookUpdate, BookDelete, BookList, LastRequests

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('last', LastRequests.as_view(), name='last'),
    path('books', BookList.as_view(), name='book_list'),
    path('view/<int:pk>', BookView.as_view(), name='book_view'),
    path('new', BookCreate.as_view(), name='book_new'),
    path('edit/<int:pk>', BookUpdate.as_view(), name='book_edit'),
    path('delete/<int:pk>', BookDelete.as_view(), name='book_delete'),
]
