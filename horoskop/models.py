from django.db import models
from django.urls import reverse


# Create your models here.
class Horoskop(models.Model):
    znak = models.CharField(max_length=100)
    slug = models.SlugField()
    dnevni = models.TextField()
    nedeljni = models.TextField()
    mesecni = models.TextField()
    godisnji = models.TextField()

    def __str__(self):
        return self.znak

    def get_absolute_url(self):
        return reverse('znak-detaljno', kwargs={'slug': self.slug})
