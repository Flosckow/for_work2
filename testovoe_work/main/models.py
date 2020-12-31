from django.db import models
from PIL import Image
from django.db import models



# для главной страницы
class MainProduct(models.Model):
    title = models.CharField('Заголовок', max_length=25)
    description = models.TextField(max_length=350)


class Gallery(models.Model):
    image = models.ImageField(upload_to='media')
    main_product = models.ForeignKey(MainProduct, on_delete=models.CASCADE, related_name='images')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)


# для продуктов
class Product(models.Model):
    header = models.CharField('Заголовок', max_length=25)
    image = models.ImageField(upload_to='media/product')
    description = models.TextField(max_length=350)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ListTitle(models.Model):
    main_title = models.TextField(max_length=150)
    title = models.CharField(max_length=50)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='headers')


