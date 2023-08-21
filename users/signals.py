from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(pre_save, sender=User)
def pre_save_receiver(sender, instance, **kwargs):
    """
    Signal receiver to print the current state of the object before saving.
    """
    print("Current state before saving:")
    print(instance.__dict__)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    print("Current state after saving:")
    print(instance.__dict__)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()