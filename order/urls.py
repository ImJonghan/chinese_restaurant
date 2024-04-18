from django.urls import path
from . import views

app_name='order'
urlpatterns = [   
    path('order_detail/<int:pk>/', views.order_detail, name='order_detail'),
    path('modify_cart/', views.modify_cart, name='modify_cart'),
    ]
