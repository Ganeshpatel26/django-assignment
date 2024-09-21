import threading
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import time

def trigger_signal_view(request):
    print(f"View thread ID: {threading.get_ident()}")
    base_username = 'transaction_user'
    unique_username = f"{base_username}_{int(time.time())}"  # Append timestamp to username
    
    user = User.objects.create(username=unique_username)
    return HttpResponse(f"User '{unique_username}' created successfully!")

def home_view(request):
    return HttpResponse("Welcome to the homepage!")
