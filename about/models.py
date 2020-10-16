from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    sub_text = models.CharField(max_length=300)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
