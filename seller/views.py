from django.shortcuts import render
from .models import Food
# Create your views here.
# 자신이 판매하는 상품 리스트를 보여주기
# -> 전체 Food에서 특정 user(판매자)인 food만 가져온다.
# -> 전체 Food에서 내가 올린 food만 filter한다.
# Food.objects.all().filter(조건)
# 상품 등록 기능
def seller_index(request):
    foods = Food.objects.filter(user=request.user)
    context={
        'object_list': foods
    }
    return render(request, 'seller/seller_index.html', context)