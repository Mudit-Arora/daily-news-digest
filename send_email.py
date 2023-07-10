import ssl, smtplib

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "YOUR_EMAIL_ID"
    password = "YOUR_PASSWORD"

    receiver = "OTHER_EMAIL_ID"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)