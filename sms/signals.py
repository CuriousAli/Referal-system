from django.db.models.signals import post_save
from django.dispatch import receiver

from phone.models import User
from .models import Sms_Code


@receiver(post_save, sender=User)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    if created:
        Sms_Code.objects.create(user=instance)