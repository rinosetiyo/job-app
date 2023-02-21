from django.db import models

# Create your models here.
NEWSLETTER_OPTION = [('w', 'Weekly'), ('M', 'Monthly')]


class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    option = models.CharField(max_length=2, choices=NEWSLETTER_OPTION)

    # def __str__(self):
    #     return self.first_name
