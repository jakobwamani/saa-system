from django.db import models
from datetime import date
class stock(models.Model):
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)
    category = models.CharField(max_length=200)
    selling_price = models.IntegerField(default=0)
    pub_date = models.DateField(default=date.today)

    def __str__(self):
        return self.product_name
    