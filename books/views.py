from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})

#check for is_admin
def add_book(request):
    #allow an admin to add books to the website
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect("show_book", pk=book.pk)
        else:
            form = BookForm()
    return render(request, "books/add_book.html", {"form": form})

def show_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/show_book.html", {"book": book})