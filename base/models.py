from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Library_DB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title

        
