from django.contrib import admin
from django.utils.safestring import mark_safe

from PIL import Image
from django.db import models


class MainProduct(models.Model):
    title = models.CharField('Заголовок', max_length=25)
    description = models.TextField(max_length=350)


class Gallery(models.Model):
    image = models.ImageField(upload_to='main_product')
    main_product = models.ForeignKey(MainProduct, on_delete=models.CASCADE, related_name='images')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 1024 or img.width > 1280:
            output_size = (1024, 1280)
            img.thumbnail(output_size)
            img.save(self.image.path)


