from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control p-4 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control p-4 border border-gray-200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control p-4 border border-gray-200'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control p-4 border border-gray-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control p-5 border border-gray-200'
            }),
                    }
