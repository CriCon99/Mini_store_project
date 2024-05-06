from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart', views.CartView.as_view(), name = 'cart'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name = 'add_to_cart')
]

