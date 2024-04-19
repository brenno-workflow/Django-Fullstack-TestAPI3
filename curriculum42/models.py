from django.db import models

# Create your models here.
from django.urls import reverse

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)    
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):

        # Retorna para a tela de criação
        #return reverse("user-new")
        
        # Vai direto para a tela de listagem
        return reverse("user-list")