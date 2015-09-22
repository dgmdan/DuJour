from django.db import models

# Create your models here.
class Order(models.Model):
	order_id = models.IntegerField()
	user_id = models.IntegerField()
	restaurant_id = models.IntegerField()
	add_date = models.DateTimeField()
	order_item = models.CharField(max_length=100)
	comments = models.TextField(blank=True)
