from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index),
    path('details', views.details, name='details'),
    path('<int:category_id>', views.get_products_by_category_id),
    path('<str:category>', views.get_products_by_category),
]