from django.db import models

# Create your models here.
class EventDetails(models.Model):
    name = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    cover_image = models.ImageField(upload_to = "uploads/")
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name