import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import configure_logging
import logging

load_dotenv(override=True)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
logging.info(f"initializing libiraries and passwords {SMTP_PORT} ,{SMTP_SERVER}, EMAIL_ADDRESS, EMAIL_PASSWORD")

def send_email(recipient_email, subject, body, attachment_path=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient_email
        msg["Subject"] = subject
        logging.info("Sending Email to recipient {}".format(recipient_email))

        msg.attach(MIMEText(body, 'plain'))

        if attachment_path:
            with open(attachment_path, "rb") as file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={os.path.basename(attachment_path)}"
                )
                msg.attach(part)
                logging.info("Reading and attaching the files")

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
            logging.info(f"loggin in and sending email")

        logging.info("Email Sent Successfully")
    except Exception as e:
        logging.exception("Exception occurred while sending email {}".format(e))

if __name__ == "__main__":
    recipient = ""
    subject = "Code is successfully workimg"
    body = "Please find attached email with attache"
    attachment_path = r"C:\Users\Naman\OneDrive - ImpactQA\Desktop\Forcx"
    send_email(recipient, subject, body, attachment_path)
    logging.info(f"Sending email with details {recipient}, {subject}, {body}, {attachment_path}")