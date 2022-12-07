# NAME : D KARTHIK SAINADH REDDY
# REGISTRATION NUMBER : 124157018
# CSE CYBER SECURITY AND BLOCKCHAIN TECHNOLOGY
# COMPUTER NETWORKS PROJECT 
# PROJECT NAME : MASS MAILER USING SMTP AND MIME
# Slow Mode

# ------------- required libraries --------------
from fileinput import filename
from smtplib import SMTP
from csv import reader,writer
from tkinter import INSERT
import time
import smtplib
from re import match
from datetime import date, datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from csv import reader
from datetime import datetime
import time
import os
#-------------------------------------------------

#----------- details -----------------------------
sender_mail_id = 'mail@gmail.com'
sender_app_password = 'password'
msg_body = """"""
msg_subject = """"""
recievers = []
writer_obj = None
#------------------------------------------------

#----------- global initiation of connections ---
smtp,msg=None,None
def init_connection():
    global smtp,msg,msg_body,msg_subject,sender_mail_id,sender_app_password,writer_obj
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

def decide_recievers(filename = None):
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
    print("to : ", to)
    with open("mail_recievers.txt") as file:
        recievers = file.read().split(",")
    recievers += to
    recievers = list(set(recievers))
    print("recievers : ",recievers)
   

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
    global sender_mail_id,sender_app_password,recievers,smtp,msg,writer_obj
    #-----------log data creation----------------
    time_stamp = str(datetime.now())
    session_summary = time_stamp + "\n" + str(msg) + "\n" + str(recievers) + "\n" + sender_mail_id + "\n"
    log_file = open('./log.txt','a')
    log_file.write(session_summary)
    #--------------------------------------------
    try:
        for i in recievers:
            smtp.sendmail(from_addr="mailid1@gmail.com",to_addrs=[i], msg=msg.as_string())
            writer_obj.insert(INSERT, str(i)+" at time : "+str(datetime.now())+"\n")
            print(" email sent to : ", i," at time : "+str(datetime.now()))
            print()
            time.sleep(7)
    except smtplib.SMTPSenderRefused:
            print("[ERROR] SMTP Sender Refused: ", end = "")
            return 1
    except smtplib.SMTPDataError:
        print("[ERROR] SMTP Data Error: ", end = "")
        return 2
    except smtplib.SMTPAuthenticationError:
        print("[ERROR] SMTP Authentication Error: ", end = "")
        return 3
    except smtplib.SMTPServerDisconnected:
        print("[ERROR] SMTP Server Disconnected: ", end = "")
        return 4
    except:
        print("might be no internet")
        return 5
    return    

#----------- main code ---------------------------

def slow_mode_send_mails(filename=None,writer = None):
    global sender_mail_id,sender_app_password,msg_subject,msg_body,recievers,writer_obj
    writer_obj = writer
    writer_obj.insert(INSERT, "mails sent : \n")
    decide_recievers(filename)
    print("starting mass mailer slow mode")
    with open("mail_data.csv", 'r') as csvf:
        data = csvf.read().split(",")
    sender_mail_id,sender_app_password,msg_subject,msg_body = data[0], data[1], data[2], data[3]
    filter_recievers_list()
    init_connection()
    send_emails()
    time.sleep(10)
    return

# -------------------------------------------------------