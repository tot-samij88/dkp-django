from django.db import models

class OurTeamate(models.Model):
    title1 = models.CharField(max_length=100,blank=True)
    img1 = models.CharField(max_length=200,blank=True)
    title2 = models.CharField(max_length=100,blank=True)
    link1 = models.ImageField(upload_to='logo_of_teamate', blank=True)
    title1 = models.CharField(max_length=100,blank=True)
    img2 = models.CharField(max_length=200,blank=True)
    link2 = models.ImageField(upload_to='logo_of_teamate', blank=True)
    title3 = models.CharField(max_length=100,blank=True)
    img3 = models.CharField(max_length=200,blank=True)
    link3 = models.ImageField(upload_to='logo_of_teamate', blank=True)
    title4 = models.CharField(max_length=100,blank=True)
    img4 = models.CharField(max_length=200,blank=True)
    link4 = models.ImageField(upload_to='logo_of_teamate', blank=True)   

    def __str__(self):
        return self.img1
