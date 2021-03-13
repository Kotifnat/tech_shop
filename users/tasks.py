import random
import string
from celery import shared_task
from django.core.mail import send_mail

from .models import UserAccount


@shared_task
def send_message():
    send_to = ['kotata706@gmail.com',]
    send_mail(
        'Subject here',
        'Here is the message.',
        None,
        send_to,
        fail_silently=False,
    )
    return f'Mail sent to{send_to}'
