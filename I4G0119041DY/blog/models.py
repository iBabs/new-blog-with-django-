from django.db import models
from django.contrib.auth import get_user_model





class Post(models.Model):
    Tittle = models.CharField(max_length= 200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE,)
    created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return self.Tittle

        # Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.

 