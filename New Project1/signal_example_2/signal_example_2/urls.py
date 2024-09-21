from django.contrib import admin
from django.urls import path
from myapp2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trigger/', views.trigger_signal_view),  # For triggering the signal
    path('', views.home_view),  # Root URL
]
