import os
import sys
import time
from tkinter import INSERT
from random import randint
import smtplib
import threading
from essential_generators import DocumentGenerator
mails_res = None
class EmailSpammer:
    num_sent = 0
    gen = DocumentGenerator()
    def __init__(self, reciever_data):
        self.receiving_email = reciever_data[0]
        self.max_num_emails = int(reciever_data[1])
        self.account_ind = 0
        if len(reciever_data) == 4:
            self.subject, self.body, self.auto_gen = reciever_data[2], reciever_data[3], False
        else:
            self.auto_gen = True
        if self.auto_gen == False:
            self.random_appendage = 1
        with open("accounts.txt", "r") as infile:
            data = [line.rstrip().split(":") for line in infile]
            self.sending_email, self.sending_passwd = map(list, zip(*data))

    def start(self):
        EmailSpammer.linear_sending(self)
  
    #sequentially iterates over the accounts.txt and swtiches only when SMTP connection gets closed
    def linear_sending(self):
        global mails_res
        for i in range(self.max_num_emails):
            if isinstance(EmailSpammer.send(self, self.sending_email[self.account_ind], self.sending_passwd[self.account_ind]), int):
                if self.account_ind != len(self.sending_email) - 1:
                    self.account_ind += 1
                else:
                    self.account_ind = 0
            curr_email = self.sending_email[self.account_ind]
            print(f"[{i + 1}/{self.max_num_emails}] total emails have been sent. The current email is {curr_email}")
        print("\nDONE !!!")
        mails_res.insert(INSERT, "spamming done")


    def send(self, sending_email, sending_passwd):
        gen = EmailSpammer.gen
        if self.auto_gen:
            full_subject = gen.sentence()
            full_body = gen.paragraph()
        elif self.random_appendage == 1:
            full_subject = self.subject + " {}".format(gen.word())
            full_body = self.body
        else:
            full_subject = self.subject
            full_body = self.body
        msg = ('Subject: {}\n\n{}'.format(full_subject, full_body)).encode(encoding='UTF-8', errors ='strict')
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(sending_email, sending_passwd)
            server.sendmail(sending_email, self.receiving_email, msg)
        except KeyboardInterrupt:
            print("\nquitting...")
            sys.exit()
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

    def prompt(str):
        while True:
            try:
                response = int(input(str))
                if response not in range(50):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid Input")
            except KeyboardInterrupt:
                print("quitting...")
                sys.exit()
        return response

def spammer_code(RECIEVING_EMAIL, NUM_EMAILS=10, SUBJECT="we are spamming", BODY = "email spammer spamming your mail box",writer = None ):
    global mails_res
    mails_res = writer
    reciever_data = [RECIEVING_EMAIL, NUM_EMAILS, SUBJECT, BODY]
    if len(reciever_data) not in [2, 4]:
        raise Exception("INVALID ARGUMENTS")
        sys.quit()
    else:
        atomic_bomb = EmailSpammer(reciever_data)
        atomic_bomb.start()
    print("spamming finished")
