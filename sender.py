import csv
from email import encoders
import email
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"

sender_email = "burningleafofficial@gmail.com"

password = getpass("Type password and press enter: ")

subject = "Greetings from Burning Leaf!"

message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = subject

hyperlink1 = MIMEText(u'<a href="https://www.youtube.com/watch?v=m7_FyMhcZoY">Youtube</a>','html')
hyperlink2 = MIMEText(u'<a href="https://onerpm.link/223036832451">streaming services.</a>','html')
hyperlink3 = MIMEText(u'<a href="https://www.youtube.com/watch?v=r3Beyijp0vM&list=PLJG81nC446VyPzlQsdtK5vmg20rNitMwV">here.</a>','html')

text1 =  MIMEText("""\
Greetings!

We are Burning Leaf, an alt/groove metal band from Pirot, Serbia, and we've just released our debut album called "Hold the Tides Away".
We'd be incredibly thankful if you could share it, or even review it if you'd like. 
You can find the album in full on """) 
text2 = MIMEText(" as well as on all bigger ")
text3 = MIMEText(" We also have a playlist with stylized lyrics videos for all the songs, which you can find ")
text4 = MIMEText("""
If you have any questions, or if you're interested and you'd like to find out the story behind the album itself, feel free to contact us! We're more than eager to answer all the questions you may have.

In case you require them, you can find our album cover image and our band photo in the attachments below.

Thank you for your time!

All the best.

-Burning Leaf
    """)

message.attach(text1)
message.attach(hyperlink1)
message.attach(text2)
message.attach(hyperlink2)
message.attach(text3)
message.attach(hyperlink3)
message.attach(text4)

attachments = ["BurningLeaf_Landscape.png", "BurningLeaf_CloseUp.jpg"]

# Loop through image files in binary mode
for at in attachments:
    with open(at, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    part.add_header(
    "Content-Disposition",
    f"attachment; filename= {at}",
    )
    message.attach(part)

text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    with open("email_list.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            print(f"Sending email to {name}")
            # message["To"] = email
            server.sendmail(sender_email, email, text)