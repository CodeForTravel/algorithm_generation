from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from test_assesment.apps.user.models import User as User_model


# User = get_user_model()


@receiver(post_save, sender=User_model)
def add_user_to_grou(sender, instance, created, **kwargs):
    print("==============")
    print(created)
    if created:
        if instance.user_type == User_model.UserTypes.STAFF:
            group, _ = Group.objects.get_or_create(name="Staff")
        elif instance.user_type == User_model.UserTypes.ADMIN:
            group, _ = Group.objects.get_or_create(name="Admin")
        else:
            group, _ = Group.objects.get_or_create(name="Geneal")
        instance.groups.add(group)