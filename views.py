from django.shortcuts import render, redirect 
from .models import Books, Authors

def index(request):
    context = {
        'all_books': Books.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(request):
    if request.method =="POST":
        Books.objects.create(
            title=request.POST['title'],
            desc=request.POST['add_book']
        )
    return redirect('/')

def display(request, book_id):
    context = {
        'this_book': Books.objects.get(id=book_id),
        'all_authors': Authors.objects.all()
    }
    return render(request, 'book.html', context)
