from django.db import models

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.task
