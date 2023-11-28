from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index),
    path('<slug:slug>', views.details, name='product_details'),
    path('<int:category_id>', views.get_products_by_category_id),
    path('<str:category>', views.get_products_by_category, name='products_by_category'),
]