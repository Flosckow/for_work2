from django.contrib import admin
from .models import Gallery, MainProduct
from main.models import Product


# class ProductInline(admin.TabularInline):
#     fk_name = 'main_product'
#     model = Product


class GalleryInline(admin.TabularInline):
    fk_name = 'main_product'
    model = Gallery
    readonly_fields = ['image_img']

    def image_img(self, obj):
        from django.utils.safestring import mark_safe
        return mark_safe(f'<img src="{obj.image.url}" width="150" height="150"')

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True



@admin.register(MainProduct)
class MainProductAdmin(admin.ModelAdmin):

    list_display = ['title', 'description']
    fields = ['description', 'title']
    inlines = [GalleryInline]






