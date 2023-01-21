from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()
model_list = [
    User
]

admin.site.register(model_list)