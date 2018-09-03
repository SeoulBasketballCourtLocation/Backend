from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Gu(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Dong(models.Model):
    gu = models.ForeignKey(Gu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    gu = models.ForeignKey(Gu, on_delete=models.CASCADE)
    dong = models.ForeignKey(Dong, on_delete=models.CASCADE)
    detail = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.city}시 {self.gu}구 {self.dong}동 {self.detail}'

