from django.db import models
from django.urls import reverse
from django.views import generic

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    filetype = models.CharField(max_length=15)
    quantity = models.IntegerField()
    price = models.IntegerField()
    file_location = models.CharField(max_length=1000000)
    sold = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)

    #owner = models.IntegerField()

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "name": self.name,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
