from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.core.mail import send_mail
from django.conf import settings
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialLogin
from allauth.account import app_settings as allauth_settings
from allauth.socialaccount import providers
from allauth.socialaccount.providers import registry
from allauth.socialaccount import app_settings as allauth_settings

def email_verification(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            otp = generate_otp()  # You need to implement this function
            send_mail(
                'Email Verification OTP',
                f'Your OTP is: {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return render(request, 'email_verification_success.html', {'email': email})
    return render(request, 'email_verification.html')


def generate_otp():
    # Implement your OTP generation logic here
    return '123456'  # For demonstration, you can replace it with your own logic

def choice(request):
    return render(request, "choice.html")


