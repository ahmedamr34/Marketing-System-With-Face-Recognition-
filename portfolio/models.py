from django.db import models

class portfolio (models.Model):
    PorName = models.CharField(max_length=255)
    PorDisc = models.TextField()
    PorImg = models.ImageField(upload_to='Service_images/', null=False, blank=False)

    def __str__(self):
        return self.PorName
