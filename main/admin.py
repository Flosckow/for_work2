from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, ListTitle, HeadListTitle


class HeadInline(admin.TabularInline):
    fk_name = 'product_q'
    model = HeadListTitle


class TitleProduct(admin.TabularInline):
    fk_name = 'product'
    model = ListTitle


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_filter = ['created']
    list_display = ['image_img', 'header', 'description']
    readonly_fields = ['image_img', ]
    fields = ['header', 'image_img', 'image', 'description']
    inlines = [TitleProduct, HeadInline]

    def image_img(self, obj):
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="60"')

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True





