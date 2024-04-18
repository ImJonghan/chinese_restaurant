from django.shortcuts import render
from seller.models import Food
from .models import Cart
# Create your views here.
def order_detail(request, pk):
    food = Food.objects.get(pk=pk)
    context = {
        'object':food
    }
    return render(request, 'order/order_detail.html', context)

from django.http import JsonResponse
def modify_cart(request):
    # A사용자가 카트에 담은 B음식에 대해서 수량을 조정하는 내용
    # 응답 : 새롭게 변경된 수량, 전체 카트 음식 수량
    # 어떤 사용자?
    user = request.user
    # 어떤 음식?
    food_id = request.POST['foodId']
    food = Food.objects.get(pk=food_id)
    # 카트 정보
    cart, created = Cart.objects.get_or_create(food=food, user=user)
    # 수량 업데이트
    cart.amount += int(request.POST['amountChange'])
    if cart.amount>0:
        cart.save()
    # Json
    context = {
        'newQuantity' : cart.amount,
        'totalQuantity' : cart.amount,
        'message':'성공',
        'success':True
    }
    return JsonResponse(context)