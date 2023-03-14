
from rest_framework import serializers
from .models import BooksModel


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooksModel
        # fields = '__all__'
        fields = ['id','name' , 'desc' , 'author' , 'price']
