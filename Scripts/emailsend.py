import smtplib
import datetime as dt
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# def send_email(content):
#     my_email = "nastkozak96@gmail.com"
#     my_password = "dokfztdikqvjzmko"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(from_addr=my_email, to_addrs="knoppix123@gmail.com", msg=content)


# send_email()

def send_email(subject, message):
# Email configuration
    sender_email = "nastkozak96@gmail.com"
    sender_password = "dokfztdikqvjzmko"
    recipient_email = "knoppix123@gmail.com"
    # Create an SMTP object
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    # Start TLS encryption
    server.starttls()
    # Log in to your Gmail account
    server.login(sender_email, sender_password)
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    # Quit the SMTP server
    server.quit()


def send_result(departure,arrival,amount, desired_price):
    if int(amount.replace("$", "")) < desired_price:
        subject = f"Good Deal from {departure} to {arrival}"
        amount = f"Price from {departure} to {arrival} is " + amount
        send_email(subject,amount)


