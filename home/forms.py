from django import forms
from .models import Book

class Books_Form(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        
        

