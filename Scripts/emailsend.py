import smtplib
import datetime as dt
import random

def send_email(content):
    my_email = "nastkozak96@gmail.com"
    my_password = "dokfztdikqvjzmko"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="knoppix123@gmail.com", msg=content)


# send_email()