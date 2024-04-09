from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=20)
    product_detail = models.CharField(max_length=20)
    product_quantity = models.IntegerField()
    total_bill = models.IntegerField()
    choice = [('Online', 'ONLINE'), ('Cash', 'CASH')]
    payment_mode = models.CharField(max_length=10, choices=choice)

