from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=300, blank=True)  #Subtítulo opcional
    content = RichTextField()  
    image = models.ImageField(upload_to='pages/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
