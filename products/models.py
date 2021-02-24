from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


def get_upload_path(instance, filename):
    name = instance.product.name
    return f'products/{name}/{filename}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    tag = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)

    def __str__(self):
        return self.image.name


class Tag(models.Model):
    name = models.CharField(max_length=25, default=1)

    def __str__(self):
        return self.name
