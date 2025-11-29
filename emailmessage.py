import smtplib
import ssl
from email.message import EmailMessage
\
    
EMAIL = "anuragnagwan900@gmail.com"
APP_PASSWORD = "pszk pufz wgpl caao"
RECEIVER = "anuragnagwan717@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "bhai  ky chal rha hai jindagi me....."

msg.set_content("ky re bete ky haal hai re......")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)