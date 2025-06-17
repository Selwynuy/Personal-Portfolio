"""
URL configuration for the main app.
"""
from django.urls import path
from . import views
from .views import timeline_events_ajax

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('ajax/timeline/', timeline_events_ajax, name='timeline_events_ajax'),
] 