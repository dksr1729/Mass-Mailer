# NAME : D KARTHIK SAINADH REDDY
# REGISTRATION NUMBER : 124157018
# CSE CYBER SECURITY AND BLOCKCHAIN TECHNOLOGY
# COMPUTER NETWORKS PROJECT 
# PROJECT NAME : MASS MAILER USING SMTP AND MIME
# Pro mode

# ------------- required libraries --------------
from fileinput import filename
from csv import reader,writer
from smtplib import SMTP
import smtplib
from re import match
from tkinter import INSERT
import time
from datetime import date, datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from csv import reader
import os
#-------------------------------------------------

#----------- details -----------------------------
sender_mail_id = '09e80z@gmail.com'
sender_app_password = 'qpqltegidfzwuixm'
msg_body = """"""
msg_subject = """"""
recievers_from_box = ["dksreddy1729@gmail.com","1729dksr@gmail.com"]
recievers_from_file = []
recievers = recievers_from_box + recievers_from_file
writer_obj = None
#------------------------------------------------

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
    with open("mail_recievers.txt") as file:
        recievers = file.read().split(",")
    recievers += to
    recievers = list(set(recievers))
    print("recievers : ",recievers)
 
#----------- global initiation of connections ---
smtp,msg=None,None
def init_connection():
    global smtp,msg,msg_body,msg_subject,sender_mail_id,sender_app_password,recievers
    try:
        smtp = SMTP('smtp.gmail.com', 587)
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

def read_data_from_csv(filename):
    to = []
    with open(filename, mode ='r')as file:
        csvFile = reader(file)
        next(csvFile)
        for lines in csvFile:
                for ele in lines:
                    to.append(ele)
    return to

#-------------- mail id validation ---------------
def check_mail_id(mail_id):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if match(pat,mail_id):
        return True
    else:
        return False

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
        smtp.sendmail(from_addr="09e80z@gmail.com",to_addrs=recievers, msg=msg.as_string())
        print(" email sent for all", recievers)
        writer_obj.insert(INSERT, str("".join(ele+"\n" for ele in recievers))+" at time : "+str(datetime.now())+"\n")
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
def pro_mode_send_mails(filename=None,writer = None):
    # call all the prerequisite functions , filters recievers , lists
    global sender_mail_id,sender_app_password,msg_subject,msg_body,recievers,writer_obj
    writer_obj = writer
    decide_recievers(filename)
    print("starting mass mailer pro mode")
    with open("mail_data.csv", 'r') as csvf:
        data = csvf.read().split(",")
    sender_mail_id,sender_app_password,msg_subject,msg_body = data[0], data[1], data[2], data[3]
    filter_recievers_list()
    init_connection()
    send_emails()
    smtp.quit()
    time.sleep(5)
    return
# -------------------------------------------------------