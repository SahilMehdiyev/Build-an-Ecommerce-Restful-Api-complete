from rest_framework import serializers
from storeapp.models import Product,Category


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
            'is_active'
        ]
        
        
        
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)

    class Meta:
        model = Category
        fields = [
                  'id', 
                  'title',
                  'slug',
                  'featured_product',
                  'icon',
                  'is_active',
                  'products'
                ]
