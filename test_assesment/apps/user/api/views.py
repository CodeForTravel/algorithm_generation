from rest_framework import viewsets, generics, permissions, status

from datetime import timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from django.contrib.auth.models import Group, Permission
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import views
from rest_framework.response import Response
import uuid
from django.contrib.contenttypes.models import ContentType

from test_assesment.apps.user.api.serializers import UserSerializer
from test_assesment.apps.user.api import serializers as serializers_user
from test_assesment.apps.user.api import permissions as permissions_user
from test_assesment.apps.user.mail_service import send_custom_mail
from test_assesment.apps.user.models import PasswordResetToken


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & permissions_user.AdminOnly]
    queryset = User.objects.all()
    serializer_class = serializers_user.UserSerializer
    

class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers_user.UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.get("password")
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)
        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                token, created = Token.objects.get_or_create(user=user)
                if created:
                    token.expires_in = timedelta(minutes=1)
                    token.save()
                return Response({"token": token.key})
            else:
                return Response({"error": "Invalid credentials"}, status=400)
        except User.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=400)


class ForgotPasswordView(views.APIView):
    def post(self, request):
        email = request.data.get('email')
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'})

        # Generate a unique token and a reset URL
        token = uuid.uuid4()
        reset_url = request.build_absolute_uri(reverse('reset-password') + '?token={}'.format(token))
        # Save the token and the reset URL in the user's model
        reset_token = PasswordResetToken.objects.create(token=token, expiry_date=timezone.now() + timezone.timedelta(minutes=5), user=user)
        reset_token.save()

        # Send the email
        send_custom_mail(
            'Password reset',
            'Click on the link to reset your password: {}'.format(reset_url),
            email,
        )
        return Response({'message': 'Password reset email sent'})


class ResetPasswordView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        token = request.data.get('token')
        password = request.data.get('password')

        try:
            reset_token = PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            return Response({"success": False, "error": "Invalid token"})

        if timezone.now() > reset_token.expiry_date:
            return Response({"success": False, "error": "Token expired"})

        # Reset the password
        user = reset_token.user
        user.set_password(password)
        user.save()

        # Delete the used token from the database
        reset_token.delete()
        return Response({'message': 'Password reset successfully'})


class CustomPermissionViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated & permissions_user.AdminOnly]

    def create(self, request):
        group_name = request.data.get('group_name')
        model_name = request.data.get('model_name')
        permissions = request.data.get('permissions')
        app_name = request.data.get('app_name')

        # Get or create the group
        group = Group.objects.get(name=group_name)

        # Get the content type of the model
        content_type = ContentType.objects.get(app_label=app_name, model=model_name)

        # Assign the necessary permissions to the group
        for permission in permissions:
            if permission == 'add':
                group.permissions.add(Permission.objects.get(codename='add_'+model_name, content_type=content_type))
            elif permission == 'change':
                group.permissions.add(Permission.objects.get(codename='change_'+model_name, content_type=content_type))
            elif permission == 'delete':
                group.permissions.add(Permission.objects.get(codename='delete_'+model_name, content_type=content_type))
        return Response({"message": "Permissions have been successfully assigned to the group."}, status=status.HTTP_200_OK)
