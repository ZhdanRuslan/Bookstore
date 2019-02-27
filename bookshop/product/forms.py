from django.forms import DateInput, ModelForm

from .models import Book


class DateInput(DateInput):
    input_type = 'date'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'isbn', 'price', 'publish_date']
        widgets = {
            'publish_date': DateInput(),
        }
