from unicodedata import category
from django.http import HttpResponseNotFound
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from datetime import datetime

data = {
    'telefon': ['samsung s20', 'samsung s21', 'iphone 12'],
    'bilgisayar': ['laptop 1', 'laptop 2'],
    'elektronik': [],
}

def index(request):
    categories = list(data.keys())
    return render(request, 'index.html', {
        'categories': categories
    })


def get_products_by_category_id(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound('yanlış kategori seçimi')
    category_name = category_list[category_id - 1]
    redirect_path = reverse('products_by_category', args=[category_name])
    return redirect(redirect_path)

def get_products_by_category(request, category):
    try:
        products = data[category]
        return render(request, 'products.html', {
            'category': category,
            'products': products,
            'now': datetime.now()
        })
    except:
        return HttpResponseNotFound(f'<h1>yanlış kategori seçimi</h1>')
