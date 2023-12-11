from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from .models import Book
from django.views import View
from .forms import SearchBookForm, AddBookForm
# Create your views here.




class BookListView(ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'index.html'
    form_class = SearchBookForm
    context_object_name = 'list_of_book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context
    

class BookAddView(View):
    form_class = AddBookForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        try:
            form_errors = kwargs['errs']
        except:
            form_errors = None
        
        context = {
            'form': form,
            'form_errors': form_errors
            }
        return render(request, 'add.html', context)
                      
    def post(self, request, *args, **kwargs):
    
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:index')
        
        kwargs['errs'] = form.errors
        return self.get(request, *args, **kwargs)
        


class BookSearchView(View):
    def get(self, request, *args, **kwargs):
        title = request.GET.get('title')
        author = request.GET.get('author')
        isbn = request.GET.get('isbn')
        
        books = Book.objects.filter(
            isbn__icontains=isbn,
            title__icontains=title,
            author__icontains=author,
            )
        form = SearchBookForm()
        context = {
            'list_of_book': books,
            'form': form,
        }
        return render(request, 'index.html', context)
        
class BookDeleteView(View):
    def get(self, request, *args, **kwargs):
        book_isbn = self.kwargs['isbn']
        print(book_isbn)
        book = Book.objects.get(isbn=book_isbn)
        book.delete()
        return redirect('book:index')
    
    
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'update.html'
    success_url = reverse_lazy('book:index')
    fields = ['title', 'isbn', 'author', 'publisher']