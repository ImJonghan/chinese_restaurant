from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=200)

class Food(models.Model):
    # id
    user=models.ForeignKey(User, on_delete=models.CASCADE) # 상품 판매자
    name=models.CharField(max_length=20)
    price = models.IntegerField()
    description=models.TextField()
    image_url=models.URLField()
