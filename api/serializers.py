from rest_framework import serializers
from storeapp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'discount',
            'old_price',  
            'price',
            'image',
            'category',
            'inventory',
            'top_deal',
            'flash_sales',
            'slug',  
        ]
        

        