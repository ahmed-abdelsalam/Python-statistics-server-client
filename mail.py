import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SMTP_SERVER , STMP_PORT , EMAIL_ADDRESS , EMAIL_PASSWORD
import numpy as np


#Send Mails when reaching alerts
class Mail:

    def __init__(self,i,cpu, memory, mails):



        #Initialization
        fromaddress = EMAIL_ADDRESS
        toaddress = mails[i]
        username = EMAIL_ADDRESS
        password = EMAIL_PASSWORD

        #Message
        text = "This is the Alret Information"+'\n'+"CPU_PERCENTAGE :" + str(np.mean(cpu)) +'%\n' +"Memory_PERCENTAGE :" + str(memory) +'%\n'
        msg = MIMEMultipart()
        msg['From'] = fromaddress
        msg['To'] = toaddress
        msg['Subject'] = "Alert"
        msg.attach(MIMEText(text))

        #Connection
        try:
            server = smtplib.SMTP(SMTP_SERVER, STMP_PORT)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(username, password)
            server.sendmail(fromaddress, toaddress, msg.as_string())
            server.quit()
        except:
            print "Server cannot send an e-mail to the specified address"