from django.contrib import admin

from .models import MainProduct, Product, Gallery, ListTitle


class GalleryInline(admin.TabularInline):
    fk_name = 'main_product'
    model = Gallery


@admin.register(MainProduct)
class MainProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]


class TitleProduct(admin.TabularInline):
    fk_name = 'product'
    model = ListTitle


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [TitleProduct,]