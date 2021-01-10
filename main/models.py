
from django.db import models
from PIL import Image
from django.db import models
from django.utils import timezone


class Product(models.Model):
    header = models.CharField('Заголовок', max_length=25)
    image = models.ImageField(upload_to='product')
    description = models.TextField(max_length=350)
    created = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 860 or img.width > 1280:
            output_size = (860, 1280)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ListTitle(models.Model):
    title = models.CharField(max_length=100)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='headers')

    def __str__(self):
        return self.title


class HeadListTitle(models.Model):
    title = models.CharField(max_length=150)
    title_del = models.ForeignKey(ListTitle, on_delete=models.CASCADE, related_name='head_list')
    product_q = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='test_field')



