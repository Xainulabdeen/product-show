from django.urls import path
from .views import ProductList,ProductListCreate

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
  path('products-create/', ProductListCreate.as_view(), name='product-create'),
]
