from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from test_assesment.apps.product.api import serializers as serializers_product
from test_assesment.apps.user.api import permissions as permissions_user
from test_assesment.apps.product import models as models_product
from test_assesment.apps.user.api import pagination as pagination_global




class ProductViewSet(viewsets.ModelViewSet):
    queryset = models_product.Product.objects.all()
    serializer_class = serializers_product.ProductSerializer
    pagination_class = pagination_global.GlobalPagination
    permission_classes = [IsAuthenticated]

 
        