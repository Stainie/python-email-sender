import smtplib, ssl

port = 465
smtp_server = "smtp@gmail.com"

sender_email = "test@gmail.com"
receiver_email = "test2@gmail.com"
password = input("Type password and press enter: ")

message = """\
    Greetings!

We are Burning Leaf, an alt/groove metal band from Pirot, Serbia, and we've just released our debut album called "Hold the Tides Away".
We'd be incredibly thankful if you could share it, or even review it if you'd like. 
You can find the album in full on Youtube (https://www.youtube.com/watch?v=m7_FyMhcZoY) as well as all bigger streaming services (such as Spotify, Deezer).
We also have a playlist with stylized lyrics videos for all the songs, which you can find here: https://www.youtube.com/watch?v=r3Beyijp0vM&list=PLJG81nC446VyPzlQsdtK5vmg20rNitMwV

In case you have any questions, or if you're interested and you'd like to find out the story behind the album itself, feel free to contact us! We're more than eager to answer all the questions you may have.

Thank you for your time!

All the best,
Burning Leaf
    """

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context) as server:
    server.login(sender_email, password)
    server.send_message(message, sender_email, receiver_email)