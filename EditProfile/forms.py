from django import forms
from login.models import UserReg

# Create your models here.
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserReg
        fields = ['username','first_name', 'last_name', 'email' , 'password']