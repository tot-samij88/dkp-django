from django.db import models


class FirstSlide(models.Model):
    title = models.CharField(max_length=200)
    sub_text = models.CharField(max_length=250)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class NextSlide(models.Model):
    title = models.CharField(max_length=200,blank=True)
    sub_text = models.CharField(max_length=250,blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
