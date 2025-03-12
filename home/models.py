from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    description = models.TextField()
    quantitu = models.PositiveIntegerField()
    image = models.ImageField(upload_to='book_images/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Book"
    
    def __str__(self):
        return super().__str__()
    

        
    
