'''
import sendgrid
import os
from sendgrid.helpers.mail import *
'''

import smtplib



#AKIAIF3E7TOV4UXTTMUQ 
#Al8wnYoFZkinQGG7xg0wgjAmW8389FkjrU8jQIErtZNs 
# host email-smtp.us-west-2.amazonaws.com
# SMTP Port—25, 587, or 2587 (to connect using STARTTLS), or 465 or 2465 (to connect using TLS Wrapper).

msg_header = 'From: Sender Name saikumar.divvela@gmail.com\n' \
             'To: Receiver Name saikumar.divvela@gmail.com\n' \
             'MIME-Version: 1.0\n' \
             'Content-type: text/html\n' \
             'Subject: Any subject\n'
title = 'My title'
msg_content = '<h2>{title} > <font color="green">OK</font></h2>\n'.format(
    title=title)
msg_full = (''.join([msg_header, msg_content])).encode()

try:
    sender = "saikumar.divvela@gmail.com"
    receivers = "sai.divvela@samsung.com"
    username="AKIAIF3E7TOV4UXTTMUQ"
    password="Al8wnYoFZkinQGG7xg0wgjAmW8389FkjrU8jQIErtZNs"
    username="saikumar.divvela"
    password="neeru$123"
    #server = smtplib.SMTP('email-smtp.us-west-2.amazonaws.com:465')
    #server = smtplib.SMTP('email-smtp.us-west-2.amazonaws.com:465')
    server = smtplib.SMTP('smtp.gmail.com:587')
    print ('initializing server...')
    server.starttls()
    server.login(username, password)
    server.sendmail(sender, receivers, msg_full)         
    print ("Successfully sent email")
except Exception:
   print ("Error: unable to send email")
