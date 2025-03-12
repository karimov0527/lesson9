from django.shortcuts import render,redirect,get_object_or_404
from django.views import View

from .models import Book
from .forms import Books_Form


class Books_list(View):
    def get(self,request):
        books = Book.objects.all()
        return render(request,"home.html",{'books':books})

class Book_create(View):
    def get(self,request):
        form = Books_Form()
        return render(request,"book_create.html",{'form':form})
    def post(self,request):
        form = Books_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("books-list")
        return render(request,"book_create.html",{'form':form})
    
class Book_update(View):
    def get(self,request,pk):
        books = get_object_or_404(Book,id=pk)
        form = Books_Form(instance=books)
        return render(request,"book_update.html",{'form':form})
    
    def post(self,request,pk):
        books = get_object_or_404(Book,id=pk)
        form = Books_Form(request.POST,request.FILES,instance=books)
        if form.is_valid():
            form.save()
            return redirect("books-list")
        return render(request,'book_update.html',{'form':form})
        
class Book_delete(View):
    def get(self,request,pk):
        books = get_object_or_404(Book,id=pk)
        return render(request,'book_delete.html',{'books':books})
    
    def post(self,request,pk):
        books = get_object_or_404(Book,id=pk)
        books.delete()
        return redirect('books-list')
    
class Search_book(View):
    def get(self,request):
        q = request.GET.get('t')
        books = Book.objects.filter(name__icontains = q) 
        return render(request,'search.html',{'books':books})
    