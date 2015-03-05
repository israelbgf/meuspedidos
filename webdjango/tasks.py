from __future__ import absolute_import
from celery import shared_task
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_email(subject, from_email, to, html_content):
    msg = EmailMultiAlternatives(subject, '', from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
