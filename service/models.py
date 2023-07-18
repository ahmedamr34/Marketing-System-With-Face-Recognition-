from django.db import models

class sponsor (models.Model):
    SerName = models.CharField(max_length=255)
    SerDisc = models.TextField()
    SerImg = models.ImageField(upload_to='Service_images/', null=False, blank=False)

    def __str__(self):
        return self.SerName
