from django.db import models

# Create your models here.
class Articels(models.Model):
        title = models.CharField(max_length=120)
        body =models.TextField()
        date =models.DateTimeField()
        # price= models.DecimalField(max_digits=10, decimal_places=2)
        # price =models.TextField(default=None)
        cover = models.ImageField(upload_to='images/')

        def __str__(self):
            return  self.title
