import random
import string
from celery import shared_task
from django.core.mail import send_mail

from .models import UserAccount


@shared_task
def send_message():
    send_mail(
        'Subject here',
        'Here is the message.',
        None,
        ['kotata706@gmail.com'],
        fail_silently=False,
    )
