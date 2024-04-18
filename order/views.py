from django.shortcuts import render
from seller.models import Food
from .models import Cart
from django.db.models import Sum
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
    # "user"가 카트에 담은(cart)한 전체 음식(개별 개수 amount) 개수
    # Qusetion - Choice
    # 이 문제에 대한 초이스
    # question.choice_set
    totalQuantity = user.cart_set.aggregate(totalcount=Sum('amount'))['totalcount']
    # Json
    context = {
        'newQuantity' : cart.amount,
        'totalQuantity' : totalQuantity,
        'message':'성공',
        'success':True
    }
    return JsonResponse(context)