from django.db import models
from seller.models import Food
from django.contrib.auth.models import User
# Create your models here.

# 어떤 음식을 얼마나 카트에 담았나?

# table 생성 default 이름 : customer_cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0)