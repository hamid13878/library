from django.db import models

    
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="نام" )
    isbn = models.CharField(max_length=100,unique=True, verbose_name="شابک")
    author = models.CharField(max_length=100, verbose_name="نویسنده")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="انتشارات")
    
    def __name__(self):
        return self.title
    

