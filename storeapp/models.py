from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import User
from  django.conf import settings
from UserProfile.models import Customer

from django.utils.text import slugify
# Create your models here.

        
class Category(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    slug = models.SlugField(default= None)
    featured_product = models.OneToOneField('Product', on_delete=models.CASCADE, blank=True, null=True, related_name='featured_product')
    icon = models.CharField(max_length=100, default=None, blank = True, null=True)
    is_active = models.BooleanField(default=False)
    

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)
        
    @classmethod
    def get_all_category(cls):
        return cls.objects.filter(is_active=True)
                    
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    discount = models. BooleanField(default=False)
    image = models.ImageField(upload_to = 'img',  blank = True, null=True, default='')
    old_price = models.FloatField(default=100.00)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    slug = models.SlugField(default=None, blank=True, null=True)
    inventory = models.IntegerField(default=5)
    top_deal=models.BooleanField(default=False)
    flash_sales = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    @property
    def price(self):
        if self.discount:
            new_price = self.old_price - ((30/100)*self.old_price)
        else:
            new_price = self.old_price
        return new_price
    
    @classmethod
    def get_all_products(cls):
        return cls.objects.filter(is_active=True)
    
    @property
    def img(self):
        if self.image == "":
            self.image = ""
        
        return self.image

    def __str__(self):
        return self.name

class Cart(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=100)
    

    @property
    def num_of_items(self):
        cartitems = self.cartitems_set.all()
        qtysum = sum([ qty.quantity for qty in cartitems])
        return qtysum
    
    @property
    def cart_total(self):
        cartitems = self.cartitems_set.all()
        qtysum = sum([ qty.subTotal for qty in cartitems])
        return qtysum

    def __str__(self):
        return str(self.cart_id)

class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity = models.IntegerField(default=0)
    
    
    @property
    def subTotal(self):
        total = self.quantity * self.product.price
        
        return total
    
   

class SavedItem(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, null = True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    added = models.IntegerField(default=0)
    
    
    
    def __str__(self):
        return str(self.id)
    
