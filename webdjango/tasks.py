from django.core.mail import EmailMultiAlternatives
from webdjango.celery import app

@app.task
def send_email(subject, from_email, to, html_content):
    msg = EmailMultiAlternatives(subject, '', from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()