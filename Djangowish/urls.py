# urls.py
from django.urls import path, include
from .views import  email_verification, choice

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('email-verification/', email_verification, name='email_verification'),
    path('', choice, name='choice')
]
