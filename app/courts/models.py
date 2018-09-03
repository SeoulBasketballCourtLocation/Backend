from django.db import models

class Court(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    coordinate_x = models.CharField(max_length=255)
    coordinate_y = models.CharField(max_length=255)
    no_basket = models.IntegerField()
    bench = models.BooleanField(default=False)
    showerbox = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)

    def __str__(self):
        return self.name

