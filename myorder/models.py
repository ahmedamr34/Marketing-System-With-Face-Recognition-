from django.db import models
from login.models import UserReg
from login.admin import RegularUserProxy
from websites.models import AddHolder



class Category(models.Model):
    Cat_name=models.CharField(max_length=100)

    def __str__(self):
        return self.Cat_name

class Order(models.Model):
    user = models.ForeignKey(RegularUserProxy, on_delete=models.CASCADE, to_field='username')
    company_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='order_Category')
    product_description = models.CharField(max_length=500)
    AddHolder_name = models.ForeignKey(AddHolder, on_delete=models.CASCADE,related_name='order_AddHolder')
    place = models.CharField(max_length=500 ,default="null")
    image = models.ImageField(upload_to='order_images')
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.product_name
    
