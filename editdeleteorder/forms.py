from django import forms
from myorder.models import Order

class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['company_name', 'brand_name', 'product_name' , 'product_description' , 'image',]

class DeleteOrderForm(forms.Form):
    confirm_delete = forms.BooleanField(required=True)

    class Meta:
        model = Order
        fields = []  # Empty list, as we don't need to modify any specific fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['confirm_delete'].label = 'Confirm Delete'  # Custom label for the checkbox
