# NAME : D KARTHIK SAINADH REDDY
# REGISTRATION NUMBER : 124157018
# CSE CYBER SECURITY AND BLOCKCHAIN TECHNOLOGY
# COMPUTER NETWORKS PROJECT 
# PROJECT NAME : MASS MAILER USING SMTP AND MIME
# Main file

# ------------- required libraries --------------
from fileinput import filename
from smtplib import SMTP
from csv import reader,writer
from re import match
from datetime import date, datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from csv import reader
import time
import os
#-------------------------------------------------

#----------- details -----------------------------
sender_mail_id = '09e80z@gmail.com'
sender_app_password = 'qpqltegidfzwuixm'
msg_body = """"""
msg_subject = """"""
recievers = []
#------------------------------------------------

#----------- global initiation of connections ---
smtp,msg=None,None
def init_connection():
    global smtp,msg,msg_body,msg_subject,sender_mail_id,sender_app_password
    try:
        smtp = SMTP('smtp.gmail.com', 587,timeout=(len(recievers)*15 + 20))
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_mail_id, sender_app_password)
        msg = MIMEMultipart()
        msg['Subject'] = msg_subject
        text = msg_body
        attach_files()
        msg.attach(MIMEText(text))
    except:
        print("an error has occured ::::: might be no internet")
#------------------------------------------------

#-------------- mail id validation ---------------
def check_mail_id(mail_id):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if match(pat,mail_id):
        return True
    else:
        return False

def decide_recievers(filename):
    global recievers
    with open("attach_csv_address.txt") as file:
        filename = file.read()
    to = []
    if(filename != None):
        with open(filename, mode ='r')as file:
            csvFile = reader(file)
            next(csvFile)
            for lines in csvFile:
                    for ele in lines:
                        to.append(ele)
    with open("mail_recievers.py",'a') as csvfile:
            csvwriter  = writer(csvfile)
            for ele in to:
                csvwriter.writerow(ele)
                csvwriter.writerow(",")
    with open("mail_recievers.py") as file:
        recievers = file.read().split(",")
    

def filter_recievers_list():
    global recievers
    temp_recievers=[]
    invalid_reciever_id=[]
    for reciever in recievers:
        validity = check_mail_id(reciever)
        if(validity == True):
            temp_recievers.append(reciever)
        else:
            invalid_reciever_id.append(reciever)
    recievers = temp_recievers
    print("detected invalid reciever mail ids : ",invalid_reciever_id)
    print("detected valid mail ids : ",recievers)
#-------------------------------------------------

def attach_files():
    global msg
    with open("attach_address.txt") as attachment_file:
        attachment = attachment_file.read()
        print("data tester ", attachment)
    try:
        with open(attachment, 'rb') as f:
            file = MIMEApplication(f.read(), name=os.path.basename(attachment))
            file['Content-Disposition'] = f'attachment; \
            filename="{os.path.basename(attachment)}"'
            msg.attach(file)
    except:
        print("unable to attach file")

#-------------------------------------------------

def send_emails():
    global sender_mail_id,sender_app_password,recievers,smtp,msg
    #-----------log data creation----------------
    time_stamp = str(datetime.now())
    session_summary = time_stamp + "\n" + str(msg) + "\n" + str(recievers) + "\n" + sender_mail_id + "\n"
    log_file = open('./log.txt','a')
    log_file.write(session_summary)
    #--------------------------------------------
    try:
        for i in recievers:
            smtp.sendmail(from_addr="09e80z@gmail.com",to_addrs=[i], msg=msg.as_string())
            print(" email sent to : ", i)
            time.sleep(7)
    except:
        print("no internet")
    return    

#----------- main code ---------------------------

def slow_mode_send_mails(filename=None):
    global sender_mail_id,sender_app_password,msg_subject,msg_body,recievers
    decide_recievers(filename)
    print(recievers)
    print("starting mass mailer pro mode")
    print("validating emails")
    with open("mail_data.csv", 'r') as csvf:
        data = csvf.read().split(",")
    sender_mail_id,sender_app_password,msg_subject,msg_body = data[0], data[1], data[2], data[3]
    filter_recievers_list()
    init_connection()
    send_emails()
    exit()

# -------------------------------------------------------