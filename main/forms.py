from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from main.models import Order_qq, Product


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order_qq
        fields = ('first_name', 'last_name', 'address', 'quantity', 'product')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image', 'product_item')