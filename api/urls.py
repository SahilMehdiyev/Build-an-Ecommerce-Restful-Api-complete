from django.urls import path
from . import views

urlpatterns = [
    path('products/' ,views.ProductListAPIView.as_view()),
    path('categories/' ,views.CategoryAPIView.as_view()),

]