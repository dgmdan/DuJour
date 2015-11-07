from django.db import models

# Create your models here.
class Order(models.Model):
	order_id = models.IntegerField()
	user_id = models.IntegerField()
	restaurant_id = models.IntegerField()
	add_date = models.DateTimeField()
	order_item = models.CharField(max_length=100)
	comments = models.TextField(blank=True)

class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    admin = models.BooleanField()
