from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from EmailText import EmailText
import smtplib


class SendEmail(EmailText):
    def send_email(self):
        text = self.build_email_text()
        my_data = self.input()

        # setting authentication information and the SMTP server
        gmail_user = my_data["from"]
        gmail_password = my_data["password"]
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # building the message
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = my_data["to"]
        msg['Subject'] = my_data['type_of_leave'] + " Request"

        body = text
        msg.attach(MIMEText(body, 'plain'))

        # making the connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)

        # sending the message
        text = msg.as_string()
        server.sendmail(gmail_user, my_data["to"], text)
        server.quit()


test = SendEmail()
test.send_email()
print("Email sent successfully!")