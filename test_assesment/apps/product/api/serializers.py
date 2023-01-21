from rest_framework import  serializers
from test_assesment.apps.product import models as models_product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_product.Product
        fields = ["id", "title", 'description', "quantity", "price"]




        
