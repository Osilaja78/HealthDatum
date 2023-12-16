# This module contains logic for sending
# emails to users, using gmail smtp.

from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl, smtplib
from dotenv import load_dotenv
import os


load_dotenv()

EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST = os.getenv('EMAIL_HOST')


async def send_mail(email: str, content: str):
    """
    Sends email to users.
    
    Parameters:
        email: reciever's email address.
        content: the content of the email to be sent.
    """

    email_sender = EMAIL_SENDER
    email_password = EMAIL_PASSWORD
    email_reciever = email

    subject = 'SketchSync - Real-time Witeboard.'

    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject

    em.attach(MIMEText(content, "html"))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        EMAIL_HOST,
        EMAIL_PORT,
        context=context
    ) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
