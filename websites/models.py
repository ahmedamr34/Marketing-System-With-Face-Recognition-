from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AddHolder(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    price = models.IntegerField(default=100)


    def __str__(self):
        return self.name