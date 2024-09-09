from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def send_email_token(email,token):
    try:
        subject = 'Your account needs to be verified'
        message = f'Click on the link to verify http://127.0.0.1:8000/verify/{token}'
        recipient_list = [email]  # Replace with the recipient's email
        email_from = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        return False

    return True