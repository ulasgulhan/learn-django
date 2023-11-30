from django import forms

from .models import Product


""" class ProductCreateForm(forms.Form):
    product_name = forms.CharField(label='Ürün Adı', min_length=3, max_length=20, error_messages={
        'min_length': 'min 3 karakter giriniz',
        'max_length': 'max 20 karakter giriniz'
    }, widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.DecimalField(label='Fiyat', min_value=10, max_value=10000, widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(label='Ürün Açıklaması', widget=forms.Textarea(attrs={'class':'form-control'}))
    slug = forms.SlugField(label='Url', widget=forms.TextInput(attrs={'class':'form-control'})) """


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'slug',)
        error_massages = {
            'name': {
                'required': 'name gerekli alan',
                'max_length': 'maksimum 50 karakter girebilirsiniz'
            }
        }
        labels = {
            'name': 'Ürün Adı',
            'price': 'Fiyat',
            'description': 'Ürün Açıklaması',
            'slug': 'Url'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'})
        }