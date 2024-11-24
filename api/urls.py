from django.urls import path
from . import views

urlpatterns = [
    path('products/' ,views.ProductListAPIView.as_view()),
    path('product/<int:pk>/', views.ProductListDetailView.as_view(), name='product-detail'),
    path('categories/' ,views.CategoryAPIView.as_view()),
    

]