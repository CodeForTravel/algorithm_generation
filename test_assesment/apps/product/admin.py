from django.contrib import admin
from test_assesment.apps.product import models as models_product

model_list = [

    models_product.Product,
]

admin.site.register(model_list)