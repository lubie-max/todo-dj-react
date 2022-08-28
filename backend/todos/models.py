from tkinter import TRUE
from django.db import models

# Create your models here.


class Task(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    completed= models.BooleanField(default=False)
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.pk} {self.title} - { self.description} " 