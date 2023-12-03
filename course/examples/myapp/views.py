from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductForm, UploadForm
from .models import Product, UploadModel
import random
import os


def index(request):
    products = Product.objects.filter(isActive=True).order_by('-price')

    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def list(request):
    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET['q']
        products = Product.objects.filter(name__contains=q).order_by('-price')
    else:
        products = Product.objects.all().order_by('-price')
    
    context = {
        'products': products,
    }

    return render(request, 'list.html', context)


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('list')
    else:
        form = ProductForm()
    
    return render(request, 'create.html', {
        'form': form
    })


def edit(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {
        'form': form
    })


def delete(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'delete-confirm.html', {
        'product': product
    })



def details(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product
    }

    return render(request, 'details.html', context)


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image = request.FILES['image'])
            model.save()
            return render(request, 'succsess.html')
    else:
        form = UploadForm()
    
    return render(request, 'upload.html', {
        'form': form
    })
