from django.db import models

# Create your models here.
class User(models.Model):
    id= models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,null=True)
    firstName = models.CharField(max_length=150, unique=True)
    lastName = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=30, unique=True)


# from django.contrib.auth.models import User

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    emoji = models.CharField(max_length=5, default='🍴')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.food_item.name} ({self.quantity})"
 
