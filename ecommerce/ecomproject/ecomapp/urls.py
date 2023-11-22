from django.urls import path

from django.views.generic import RedirectView

from . import views


app_name = 'ecom'

urlpatterns = [

    path('',views.inventory,name='inventory'),
    path('cart/', views.adding_cart, name='adding_cart'),
    path('search/',views.searchme, name='search_results'),
    path('<slug:c_slug>/',views.inventory,name='allproducts'),
    path('<slug:c_slug>/<slug:product_slug>/',views.product_detail,name='procat_detail'),

]