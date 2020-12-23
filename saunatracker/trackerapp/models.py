from django.db import models

# Create your models here.

class Track(models.Model):
    count = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Count: {self.count}, Time: {self.date_time}"