from django.urls import path
from . import views

app_name = 'search_it'

urlpatterns = [

    path('',views.searchme,name='searchme'),
]