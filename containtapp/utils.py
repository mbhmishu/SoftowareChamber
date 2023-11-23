from .models import*
import time
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

def send_mail_to_user():
    subject = "this email has been sent"
    message = "from django company "
    from_email = settings.EMAIL_HOST_USER
    recipient_list =["admin@gmail.com"]
    send_mail(subject, message,from_email, recipient_list)







