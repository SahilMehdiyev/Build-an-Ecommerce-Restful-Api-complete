from django_filters.rest_framework import filterset
from storeapp.models import Product, Product



class ProductFilter(filterset.FilterSet):
    class Meta:
        model = Product
        fields = {
            'category_id': ['exact'],
            'old_price': ['gt', 'lt']
            
        }    