import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal(sender, **kwargs):
    print("Signal received")
    time.sleep(2)  # Simulate a delay
    print("Signal handler executed")
