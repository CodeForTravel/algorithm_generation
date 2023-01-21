from django.core.mail import send_mail
from django.conf import settings

def send_custom_mail(subject, message, target_user):
    send_mail(
    subject,
    message,
    settings.EMAIL_NOREPLY,
    [target_user,],
    fail_silently=False,
)