from django.db import models


class AcardionSlider(models.Model):
    title1 = models.CharField(max_length=200, blank=True)
    title1_text = models.TextField(blank=True)
    title2 = models.CharField(max_length=200, blank=True)
    title2_text = models.TextField(blank=True)
    title3 = models.CharField(max_length=200, blank=True)
    title3_text = models.TextField(blank=True)
    photo = models.ImageField(upload_to='img_of_product', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title1
