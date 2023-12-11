from django import forms
from .models import Book


class SearchBookForm(forms.Form):
    title = forms.CharField(label='عنوان', max_length=100, required=False)
    author = forms.CharField(label='نویسنده', max_length=100, required=False)
    isbn = forms.CharField(label='شابک', max_length=100, required=False)
    
    
    
    

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publisher']
        labels = {
            'title': 'عنوان',
            'author': 'نویسنده',
            'isbn': 'شابک',
            'publisher': 'ناشر',
            
        }
    
    
