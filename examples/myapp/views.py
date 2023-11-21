from unicodedata import category
from django.http import HttpResponseNotFound
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

data = {
    'telefon': 'telefon kategorisindeki ürünler',
    'bilgisayar': 'bilgisayar kategorisindeki ürünler',
    'elektronik': 'elektronik kategorisindeki ürünler',
}

def index(request):
    return HttpResponse('index')

def details(request):
    return HttpResponse('details')

def get_products_by_category_id(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound('yanlış kategori seçimi')
    redirect_text = category_list[category_id - 1]
    return redirect('/products/' + redirect_text)

def get_products_by_category(request, category):
    try:
        category_text = data[category]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound('yanlış kategori seçimi')
