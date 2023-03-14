from django.contrib import admin
from .models import BooksModel

# Register your models here.

@admin.register(BooksModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'desc' , 'author' , 'price']

