from django.urls import path
from . import views

app_name='seller'
urlpatterns = [   
    path('', views.seller_index, name='seller_index'),
]
