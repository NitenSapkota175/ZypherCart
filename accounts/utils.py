import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

def send_email_token(email, token):
    try:
        subject = 'Your account needs to be verified'
        message = f'Click on the link to verify your account: http://127.0.0.1:8000/accounts/verify/{token}'
        sender= settings.DEFAULT_FROM_EMAIL
        to = [email,]
        print(email)
        send_mail(subject, message, sender, to,fail_silently=False)
    except Exception as e:
        logger.error(f"Error sending email token: {e}")
        return False
    return True