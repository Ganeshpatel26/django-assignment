import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal(sender, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")
    print(f"Signal inside transaction: {transaction.get_connection().in_atomic_block}")
