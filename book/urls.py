from django.contrib import admin
from django.urls import path, include
from .views import BookListView, BookAddView, BookSearchView, BookDeleteView, BookUpdateView

app_name = 'book'
urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('add/', BookAddView.as_view(), name='add'),
    path('search/', BookSearchView.as_view(), name='search'),
    path('delete/<str:isbn>', BookDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update')
    
]
