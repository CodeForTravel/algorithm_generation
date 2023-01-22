from rest_framework import  serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', "user_type"]


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(min_length=8, write_only=True)
    password1 = serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', "password", "password1", "user_type"]

    def validate(self, attrs):
        password1 = attrs.pop('password1', None)
        if attrs.get('password') != password1:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

