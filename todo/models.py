from django.db import models

# Create your models here.
class Todo(models.Model):
    title =models.CharField(max_length=50)
    description= models.TextField(blank=True)
    completed = models.BooleanField(default = False)
    Created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title