import smtplib


class SendEmail:

    def __init__(self):
        self.fromaddr = "tesztfiok.codeorgok@gmail.com"
        self.toaddrs = "tesztfiok.codeorgok@gmail.com"
        self.username = 'tesztfiok.codeorgok@gmail.com'
        self.password = 'Codeorgok123'

    # Writing the message (this message will appear in the email)
    def __message_text(self, applicant):
        msg = "Hello {0} {1}!\nYour registration was successful at some site.\nYour school is {2}." \
              "\nFrom now you can log in using the following applicant code: {3}\nThank you for choosing us you fool!"\
            .format(applicant.first_name, applicant.last_name, applicant.applied_school.city, applicant.applicant_code)
        return msg

    # Sending the mail
    def send_email(self, applicant):
        msg = self.__message_text(applicant)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.fromaddr, self.toaddrs, msg)
        server.quit()