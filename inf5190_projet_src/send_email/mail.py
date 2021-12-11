import yaml
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mail_address():
    with open('adresse.yaml', 'r') as f:
        data = yaml.safe_load(f)
        email = data['mail']
    
    f.close()
    return email

def send_mail(data):
    source_address = "inf5190bertrand@gmail.com"
    destination_address = mail_address
    body = "Voici les nouvelles installations ajoutées cette nuit "
    # : {}".format(data)"
    subject = "Nouvelles Installations !"
    
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = source_address
    msg['To'] = destination_address
    msg['ReplyTo'] = "steve@uqam.ca"

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(source_address, "linfOcch0uette")
    text = msg.as_string
    server.sendmail(source_address, destination_address, text)
    server.quit()