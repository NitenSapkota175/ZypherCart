import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

def send_email_token(email, token):
    try:
        subject = 'Your account needs to be verified'
        message = f'Click on the link to verify your account: http://127.0.0.1:8000/verify/{token}'
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        logger.error(f"Error sending email token: {e}")
        return False
    return True