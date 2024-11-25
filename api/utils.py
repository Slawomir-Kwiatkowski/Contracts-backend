import os
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


def send_activation_email(user, base_url):
    token = RefreshToken.for_user(user).access_token
    url = base_url() + "?token=" + str(token)
    message = f"Welcome {user.username}!\n You can activate your account by clicking the link below:\n{url}"
    send_mail(
        subject="Account activation",
        message=message,
        from_email=os.getenv("EMAIL_HOST_USER"),
        recipient_list=[user.email],
        fail_silently=False,
    )
