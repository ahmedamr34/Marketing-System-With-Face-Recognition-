from django import forms
from .models import Order 

class orderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'company_name', 'brand_name', 'product_name', 'product_price', 'product_category', 'product_description', 'AddHolder_name', 'place', 'image', 'start_date', 'end_date']