
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Mobile,Brand

class RegForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','email']
        

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields =['brand_name','brand_img','Description']
        
        
class ProductForm(forms.ModelForm):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), empty_label="Select Brand", widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Mobile
        fields = ['phone_id', 'brand', 'model_name', 'Img', 'price', 'display_size', 'processor', 'battery_capacity', 'RAM', 'internal_storage', 'is_free_delivary_available', 'is_in_stock']

class ProductForm(forms.ModelForm):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), empty_label="Select Brand", widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Mobile
        fields = ['phone_id', 'brand', 'model_name', 'Img', 'price', 'display_size', 'processor', 'battery_capacity', 'RAM', 'internal_storage', 'is_free_delivary_available', 'is_in_stock']

        widgets = {
            'model_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model Name'}),
            'Img': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'display_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Display Size'}),
            'processor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Processor'}),
            'battery_capacity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Battery Capacity'}),
            'RAM': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RAM'}),
            'internal_storage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Internal Storage'}),
            'is_free_delivary_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_in_stock': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.label = ''



class ProductComparisonForm(forms.Form):
    product1 = forms.ChoiceField(choices=[], label='Product 1')
    product2 = forms.ChoiceField(choices=[], label='Product 2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Populate choices for the dropdown fields
        product_choices = [(product.model_name, product.model_name) for product in Mobile.objects.all()]
        self.fields['product1'].choices = product_choices
        self.fields['product2'].choices = product_choices