from django.urls import path
from . import views

app_name='seller'
urlpatterns = [   
    path('', views.seller_index, name='seller_index'),
    path('add_food/', views.add_food, name='add_food'),
    path('food_detail/<int:pk>/', views.food_detail, name='food_detail'),
    path('food_delete/<int:pk>/', views.food_delete, name='food_delete'),
    ]
