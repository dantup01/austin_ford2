"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from store.models import Customer

@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_account(sender, instance, **kwargs):
    if created:
        instance.customer.save()
        instance.customer.add(Group.objects.get(name='Customer'))
"""
