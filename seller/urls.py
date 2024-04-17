from django.urls import path
from . import views

app_name='seller'
urlpatterns = [   
    path('', views.seller_index, name='seller_index'),
    path('add_food/', views.add_food, name='add_food'),
]
