from django.db import models

class MyPhoto(models.Model):
    owner = models.ForeignKey('auth.User', related_name='image')
    image = models.ImageField(upload_to='photos', max_length=254)

