from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.IntegerField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
