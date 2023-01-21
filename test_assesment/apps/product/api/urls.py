from rest_framework import routers
from django.urls import path, include
from test_assesment.apps.product.api import views as product_views


router = routers.DefaultRouter()
router.register(r'products', product_views.ProductViewSet, basename="products")


urlpatterns = [
    path("", include(router.urls)),
]