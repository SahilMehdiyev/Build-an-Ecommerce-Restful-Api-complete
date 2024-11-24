from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category','inventory', 'top_deal', 'flash_sales', 'image', 'is_active','old_price')
        }),
        ('Slug & Meta', {
            'fields': ('slug',),
        }),
    )

    list_display = ('id','name', 'category', 'price', 'inventory', 'top_deal', 'flash_sales','is_active')
    search_fields = ('name',)
    list_filter = ('category', 'is_active','top_deal', 'flash_sales')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 25
    ordering = ('name',)


# CategoryAdmin for category management
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'icon', 'featured_product','is_active')
        }),
        ('Slug', {
            'fields': ('slug',),
        }),
    )

    list_display = ('id','title', 'slug', 'featured_product','is_active')
    search_fields = ('title',)
    list_filter = ('featured_product','is_active',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 25




admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(Customer)
admin.site.register(SavedItem)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
