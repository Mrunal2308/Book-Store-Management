from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from BookStore.models import City, Author, Category, Book


# Create your views here.
@never_cache
def home(request):
    return render(request, "Bookstore/Home.html")

@never_cache
@login_required
def add_author(request):
    if request.method == "GET":
        cities = City.objects.all()
        data = {"cities" : cities}
        return render(request,"Bookstore/AddAuthor.html",data)

    else:
        a = Author()
        a.AuthorName = request.POST["tbname"]
        a.AuthorDOB = request.POST["tbdob"]
        a.AuthorGender = request.POST["ddlgender"]
        a.AuthorEmail = request.POST["tbemail"]
        a.AuthorPhone = request.POST["tbphone"]
        a.AuthorCity = City.objects.get(CityName = request.POST["ddlcity"])
        a.save()
        return redirect("displayauthor")

@never_cache
def display_author(request):
    authors = Author.objects.all()
    data = {"authors" : authors}
    return render(request,"Bookstore/DisplayAuthor.html",data)

@never_cache
def delete_author(request,id):
    a = Author.objects.get(id=id)
    a.delete()
    return redirect("displayauthor")


@login_required
def edit_author(request,id):
    author = Author.objects.get(id=id)
    cities = City.objects.all()

    if request.method == "GET":
        data = {"author":author,'cities': cities}
        return  render(request,"Bookstore/EditAuthor.html",data)

    else:
        author.AuthorName = request.POST["tbaname"]
        author.AuthorDob = request.POST["tbadob"]
        author.AuthorGender = request.POST["ddlgender"]
        author.AuthorEmail = request.POST["tbemail"]
        author.AuthorPhone = request.POST["tbphone"]
        author.AuthorCity = City.objects.get(CityName=request.POST["ddlcity"])
        author.save()
        return redirect("displayauthor")

@never_cache
@login_required
def add_book(request):
    if request.method == "GET":
        categories = Category.objects.all()
        authornames = Author.objects.all()
        data = {"categories" : categories,"authornames": authornames}

        return render(request,"Bookstore/AddBook.html",data)

    else:
        b = Book()
        b.BookName = request.POST["tbbookname"]
        b.BookDiscription = request.POST["tbdes"]
        b.BookPublishedOn = request.POST["tbdate"]
        b.BookPrice = request.POST["tbprice"]
        b.BookCategory = Category.objects.get(CategoryName= request.POST["ddlcategory"])
        b.BookAuthor = Author.objects.get(AuthorName = request.POST["ddlauthor"])
        b.save()
        return redirect("displaybook")

@never_cache
def display_book(request):
    books = Book.objects.all()
    data = {"books" : books}
    return render(request,"Bookstore/Displaybook.html",data)

@never_cache
def delete_book(request,id):
    a = Book.objects.get(id=id)
    a.delete()
    return redirect("displaybook")

@login_required
def edit_book(request,id):
    book = Book.objects.get(id=id)
    categories = Category.objects.all()
    authornames = Author.objects.all()

    if request.method == "GET":
        data = {"book" : book,'categories': categories,'authornames' : authornames}
        return  render(request,"Bookstore/-EditBook.html",data)

    else:
        book.BookName = request.POST["tbbookname"]
        book.BookDiscription = request.POST["tbdes"]
        book.BookPublishedOn = request.POST["tbdate"]
        book.BookPrice = request.POST["tbprice"]
        book.BookCategory = Category.objects.get(CategoryName=request.POST["ddlcategory"])
        book.BookAuthor = Author.objects.get(AuthorName=request.POST["ddlauthor"])
        book.save()
        return redirect("displaybook")
