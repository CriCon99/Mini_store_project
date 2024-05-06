from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product'),
    path('add-product', views.ProductCreateProduct.as_view(), name='add_product')
]
