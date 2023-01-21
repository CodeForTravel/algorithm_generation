from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()

    def __str__(self):
        return self.title