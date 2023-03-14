from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from rest_framework.response import Response
from .models import BooksModel
from django.db.models import Max,Min
from django.http import JsonResponse

# Create your views here.

def home_view(request):
    all_books = BooksModel.objects.all()
    minPrice = BooksModel.objects.aggregate(Min('price'))
    maxPrice = BooksModel.objects.aggregate(Max('price'))

    context = {'all_books':all_books , 'minPrice': minPrice ,'maxPrice':maxPrice }
    return render(request , 'home.html' , context)


def dashboard_view(request):

    return render(request , 'dashboard.html')


def addbook_view(request):

    return render(request , 'addbook.html')

def updatebook_view(request , id):

    book = BooksModel.objects.get(id = id)
    context = {'book':book}

    return render(request , 'updatebook.html' , context)



@api_view([ 'POST','GET'])
def book_view(request):

    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = BookSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

            return Response({'status':'Data Post Successfully'})
        
        return Response(serializer.errors)


    if request.method =="GET":

        all_books = BooksModel.objects.all()

        price = request.GET.get('price' , False)
        if price:
            all_books = all_books.filter(price__lte = price)

        name = request.GET.get('name' , False)
        if name:
            all_books = all_books.filter(name__startswith = name)


        serializer = BookSerializer(all_books , many = True)
        return Response(serializer.data)


@api_view(['DELETE' ,'PUT'])
def action_view(request, id):

    if request.method =='DELETE':
        book = BooksModel.objects.get(id = id).delete()

        return Response({'status':'Data Delete Successfully'})

    if request.method =='PUT':
        newbook = request.data
        print(newbook)
        oldbook = BooksModel.objects.get(id = id)

        serializer = BookSerializer(oldbook ,newbook , partial = True )
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'Data Update Successfully'})
        
        return Response(serializer.errors)

