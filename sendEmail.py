#Importing required libraries
import smtplib
from email.mime.text import MIMEText
import argparse

#Creating a parsers and adding arguments
parser = argparse.ArgumentParser(description='Send emails to specified recipients')
parser.add_argument('-s','--sender',help='email sender',required=True)
parser.add_argument('-r','--recipients',nargs='+',help='email sender',required=True)
parser.add_argument('-m','--message',type=str,help='email message',required=True)
parser.add_argument('-c','--configuration',nargs='+',help='email configuration',required=True)

#Parse arguments
args = parser.parse_args()

sender = args.sender
recipients = args.recipients
message = args.message
host = args.configuration[0]
port = args.configuration[1]

#Creating SMTP connection
server = smtplib.SMTP(host,port)

#Creating email body 
msg = MIMEText(message)
msg['From'] = sender
msg['To'] = ", ".join(recipients)


#Sending emails
server.sendmail(sender, recipients, msg.as_string())    
 
print( "Email Sent to recipients!")
