from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from storeapp.models import Product
from .serializers import ProductSerializer






class ProductListAPIView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    