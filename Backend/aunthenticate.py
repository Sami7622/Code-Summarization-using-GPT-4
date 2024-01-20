import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage

def send_email(email, subject, html):
    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        # server.ehlo()  # Can be omitted
        # server = smtplib.SMTP('localhost', 1025)
        server.starttls()
        # print("ssssss")
        server.login("mingey.abhiprayalu@yahoo.com", "Dragon@APT#3")
        # print(server)
        # Create a message
        message = MIMEMultipart()
        message['From'] = "Your Name <mingey.abhiprayalu@gmail.com>"
        message['To'] = email
        message['Subject'] = subject
        message.attach(MIMEText(html, 'html'))

        # Send the email
        server.send_message(message)
        server.quit()
        return "Email sent successfully"
    except Exception as e:
        print(f"Error sending email: {e}")
        raise e


