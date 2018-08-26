# def sendemail(first, last, username, password, email):
# sendemail("Maritn", "Ivanov","zender33", "test","martinivanov07@gmail.com")
from credentials import *


def sendemail(first_name, last_name, username, password, user_email):
    import smtplib

    mail = smtplib.SMTP(admin_email_host, admin_email_port)
    mail.ehlo()
    mail.starttls()
    mail.login(admin_email, admin_email_password)

    subject = '{} {}, your Registration in HangMan was successful!'.format(first_name,last_name)
    body = """
            Hello {},

            Welcome to HangMan!

            Username: {}
            Password: {}
           """.format(first_name, username, password)

    message = 'Subject: {}\n{}'.format(subject, body)
    mail.sendmail('{}'.format(admin_email), user_email, message)
    # mail.send
    # print('Email sent!')
    mail.close()


def sendemail_forgotten(first_name, username, password, user_email):
    import smtplib

    mail = smtplib.SMTP(admin_email_host, admin_email_port)
    mail.ehlo()
    mail.starttls()
    mail.login(admin_email, admin_email_password)

    subject = 'Your HangMan Credentials'
    body = """
            Hello {},

            You've forgotten your login details.

            Please find them below:

            Username: {}
            Password: {}
           """.format(first_name, username, password)

    message = 'Subject: {}\n{}'.format(subject, body)
    mail.sendmail('{}'.format(admin_email), user_email, message)
    # mail.send
    # print('Email sent!')
    mail.close()

# sendemail_forgotten("Maritn","zender33", "test","martinivanov07@gmail.com")


