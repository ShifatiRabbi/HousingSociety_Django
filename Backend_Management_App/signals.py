"""from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member

@receiver(post_save, sender=User)
def create_member_for_user(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(phone=instance.username, email=instance.email, password=instance.password, first_name=instance.first_name, last_name=instance.last_name)

@receiver(post_save, sender=Member)
def create_user_for_member(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(username=instance.phone, email=instance.email, password=instance.password, first_name=instance.first_name, last_name=instance.last_name)

"""