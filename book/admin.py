from django.contrib import admin
from .models import Book, Publisher
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','isbn')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address')
