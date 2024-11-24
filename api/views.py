from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from storeapp.models import Product,Category
from .serializers import ProductSerializer,CategorySerializer




class ProductListAPIView(APIView):
    def get(self,request):
        products = Product.objects.filter(is_active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class CategoryAPIView(APIView):
    def get(self,request):
        categories = Category.objects.filter(is_active=True)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
        
    
    