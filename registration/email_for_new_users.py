import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models import *
from _datetime import datetime


class SendEmail:

    def __init__(self):
        self.fromaddr = "tesztfiok.codeorgok@gmail.com"
        self.username = 'tesztfiok.codeorgok@gmail.com'
        self.password = 'Codeorgok123'

    # Writing the message (this message will appear in the email)
    def __applicant_message_text(self, new_applicant):
        message = "Hello " + new_applicant.first_name + " " + new_applicant.last_name + \
              "!\nYour registration was successful at some site.\nYour school is "\
              + new_applicant.applied_school.city + "\nFrom now you can log in using the following applicant code: "\
              + new_applicant.applicant_code + "\nThank you for choosing us you fool!"
        return message

    def __mentor_message_text(self, new_mentor):
        message = "Hello {0} {1}!\nYour registration was successful at some site.\nYour school is {2}." \
              "\nFrom now you can log in using the following mentor id: {3}\nThank you for choosing us you fool!"\
            .format(new_mentor.first_name, new_mentor.last_name, new_mentor.school.city,
                    new_mentor.id)
        return message

    # Sending the mail
    def send_applicant_email(self, new_applicant):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = new_applicant.email
        msg['Subject'] = 'New applicant registration'
        message = self.__applicant_message_text(new_applicant)
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        self.__save_email_details_to_table(msg['Subject'], message, 'Applicant registration',
                                           new_applicant.first_name + ' ' + new_applicant.last_name, msg['To'])

    def send_mentor_email(self, new_mentor):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = new_mentor.email
        msg['Subject'] = 'New mentor registration'
        message = self.__mentor_message_text(new_mentor)
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        self.__save_email_details_to_table(msg['Subject'], message, 'Mentor registration',
                                           new_mentor.first_name + ' ' + new_mentor.last_name, msg['To'])

    def __save_email_details_to_table(self, subject, msg, email_type, person, email_address):
        new_email_to_table = EmailDetails(subject=subject, message=msg[0:140], date=datetime.now(), email_type=email_type,
                     person=person, email_address=email_address)
        new_email_to_table.save()
