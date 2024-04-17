from django.shortcuts import render

# Create your views here.
def order_detail(request, pk):
    return render(request, 'order/order_detail.html')