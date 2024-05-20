from django.contrib import admin
from .models import Product, Brand, Category, Tag

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'partnumber', 'brand', 'price', 'quantity', 'category')
    search_fields = ('name', 'partnumber', 'brand__name', 'category__name')
    list_filter = ('brand', 'category')
    fieldsets = (
        (None, {
            'fields': ('name', 'partnumber', 'description', 'price', 'quantity')
        }),
        ('Related', {
            'fields': ('brand', 'category')
        }),
        ('Media', {
            'fields': ('image', 'catalog')
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)