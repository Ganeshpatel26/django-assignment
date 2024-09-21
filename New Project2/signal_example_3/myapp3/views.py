from django.db import transaction
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import time

def trigger_signal_view(request):
    with transaction.atomic():
        user = User.objects.create(username='transaction_user')
        print(f"View inside transaction: {transaction.get_connection().in_atomic_block}")
    return HttpResponse(f"User '{user}' created successfully!")
