import csv
import json
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
import smtplib
import ssl
import os
from dotenv import load_dotenv

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def create_message(sender_email, config):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = config["subject"]

    body = config["body"].format(**config["links"])
    message.attach(MIMEText(body, "plain"))

    for attachment_file in config["attachments"]:
        with open(attachment_file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_file}",
        )
        message.attach(part)

    return message

def main():
    port = 465
    smtp_server = "smtp.gmail.com"
    load_dotenv()

    sender_email = os.environ.get("SENDER_EMAIL") or input("Type your email and press enter: ")
    print(f"Sender email: {sender_email}")
    password = os.environ.get("GMAIL_APP_PASSWORD") or getpass("Type app password and press enter: ")

    config = load_config("email_config_sr.json")
    message = create_message(sender_email, config)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        with open("email_list_sr.csv") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row (column names)
            for name, email in reader:
                print(f"Sending email to {name}, {email}")
                rcpt = [] + [] + [email]
                message["To"] = email
                server.sendmail(sender_email, rcpt, message.as_string())

if __name__ == "__main__":
    main()