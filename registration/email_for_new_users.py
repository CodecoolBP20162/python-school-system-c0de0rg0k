import smtplib


class SendEmail:

    def __init__(self):
        self.fromaddr = "tesztfiok.codeorgok@gmail.com"
        self.toaddrs = "tesztfiok.codeorgok@gmail.com"
        self.username = 'tesztfiok.codeorgok@gmail.com'
        self.password = 'Codeorgok123'

    # Writing the message (this message will appear in the email)
    def __applicant_message_text(self, new_applicant):
        msg = "Hello {0} {1}!\nYour registration was successful at some site.\nYour school is {2}." \
              "\nFrom now you can log in using the following applicant code: {3}\nThank you for choosing us you fool!"\
            .format(new_applicant.first_name, new_applicant.last_name, new_applicant.applied_school.city,
                    new_applicant.applicant_code)
        return msg

    def __mentor_message_text(self, new_mentor):
        msg = "Hello {0} {1}!\nYour registration was successful at some site.\nYour school is {2}." \
              "\nFrom now you can log in using the following mentor id: {3}\nThank you for choosing us you fool!"\
            .format(new_mentor.first_name, new_mentor.last_name, new_mentor.school.city,
                    new_mentor.id)
        return msg

    # Sending the mail
    def send_applicant_email(self, new_applicant):
        msg = self.__applicant_message_text(new_applicant)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.fromaddr, self.toaddrs, msg)
        server.quit()

    def send_mentor_email(self, new_mentor):
        msg = self.__mentor_message_text(new_mentor)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.fromaddr, self.toaddrs, msg)
        server.quit()