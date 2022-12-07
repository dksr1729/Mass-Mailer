# NAME : D KARTHIK SAINADH REDDY
# REGISTRATION NUMBER : 124157018
# CSE CYBER SECURITY AND BLOCKCHAIN TECHNOLOGY
# COMPUTER NETWORKS PROJECT 
# PROJECT NAME : MASS MAILER USING SMTP AND MIME
# Main GUI

#----- required libraries -----------#
import tkinter as tk
import tkinter.font as tkFont
from csv import *
from file_loader import *
from mass_mailer_pro_mode import pro_mode_send_mails
from mass_mailer_slow_mode import slow_mode_send_mails
from email_spam_sender import spammer_code
import socket
from requests import get 
import re, uuid
import time
#------------------------------------#

#----------- global variables used---#
data=None
GLineEdit_156,GLineEdit_566,GLineEdit_567,GLineEdit_996,GLineEdit_804,GLineEdit_997,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286 = None,None,None,None,None,None,None,None,None,None,None,None,None
mail_id, mail_password, mail_subject, mail_body, recievers = "", "", "", """""", []
GLabel_1696,GLabel_1466,GLabel_3166,GButton_1345 = None,None,None,None
#------------------------------------#

class App:
    def __init__(self, root):

        #setting title
        global GButton_1345,GLineEdit_156,GLineEdit_567,GLabel_1696,GLabel_1466,GLabel_3166,GLineEdit_997,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286
        root.title("Mass mailer using python")
        root.configure(background="white")
        
        #setting window size
        width=1400
        height=800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # label
        GLabel_560=tk.Label(root)
        GLabel_560["borderwidth"] = "4px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_560["font"] = ft
        GLabel_560["fg"] = "#FFFFFF"
        GLabel_560["justify"] = "center"
        GLabel_560["text"] = "Enter Mail ID "
        GLabel_560["background"]="#357EC7"
        GLabel_560.place(x=20,y=24,width=250,height=30)

        # label
        GLabel_268=tk.Label(root)
        GLabel_268["borderwidth"] = "5px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_268["font"] = ft
        GLabel_268["fg"] = "#FFFFFF"
        GLabel_268["justify"] = "center"
        GLabel_268["text"] = "Enter Application Password"
        GLabel_268["background"]="#357EC7"
        GLabel_268.place(x=24,y=72,width=250,height=30)

        # label
        GLabel_632=tk.Label(root)
        GLabel_632["borderwidth"] = "5px"
        ft = tkFont.Font(family='Arial',size=11,weight="bold")
        GLabel_632["font"] = ft
        GLabel_632["fg"] = "#FFFFFF"
        GLabel_632["justify"] = "center"
        GLabel_632["text"] = "THE MASS MAILER PROJECT"
        GLabel_632["background"]="#041F39"
        GLabel_632.place(x=24,y=150,width=700,height=40)

        # label
        GLabel_277=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_277["borderwidth"] = "5px"
        GLabel_277["font"] = ft
        GLabel_277["fg"] = "#FFFFFF"
        GLabel_277["justify"] = "center"
        GLabel_277["text"] = "Enter subject"
        GLabel_277["background"]="#357EC7"
        GLabel_277.place(x=24,y=225,width=200,height=30)

        #label
        GLabel_764=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_764["font"] = ft
        GLabel_764["fg"] = "#FFFFFF"
        GLabel_764["justify"] = "center"
        GLabel_764["text"] = "Enter Mail Content"
        GLabel_764["background"] = "#357EC7"
        GLabel_764.place(x=24,y=270,width=200,height=30)

        #label
        GLabel_765=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_765["font"] = ft
        GLabel_765["fg"] = "#FFFFFF"
        GLabel_765["justify"] = "center"
        GLabel_765["text"] = "Mass Mailing Platform in C-S \nFor Any Organization With \nImproved SMTP, MIME using python"
        GLabel_765["background"] = "#041F39"
        GLabel_765.place(x=900,y=50,width=450,height=90)

        #label
        GLabel_766=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_766["font"] = ft
        GLabel_766["fg"] = "#FFFFFF"
        GLabel_766["justify"] = "center"
        GLabel_766["text"] = "Developed by : \nD KARTHIK SAINADH REDDY\n124157018\nCSE CSBC"
        GLabel_766["background"] = "#041F39"
        GLabel_766.place(x=900,y=600,width=450,height=90)

        #label
        GLabel_286=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_286["font"] = ft
        GLabel_286["fg"] = "#FFFFFF"
        GLabel_286["justify"] = "center"
        GLabel_286["text"] = "Enter recievers list"
        GLabel_286["background"] = "#357EC7"
        GLabel_286.place(x=24,y=470,width=200,height=30)

        #input of mail id
        GLineEdit_113=tk.Entry(root)
        GLineEdit_113["borderwidth"] = "3px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLineEdit_113["font"] = ft
        GLineEdit_113["fg"] = "#000000"
        GLineEdit_113["justify"] = "center"
        GLineEdit_113["text"] = "example@gmail.com"
        GLineEdit_113.place(x=300,y=24,width=425,height=30)

        #input of application password
        GLineEdit_804=tk.Entry(root)
        GLineEdit_804["borderwidth"] = "3px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLineEdit_804["font"] = ft
        GLineEdit_804["fg"] = "#000000"
        GLineEdit_804["justify"] = "center"
        GLineEdit_804["text"] = "applicationpassword"
        GLineEdit_804.place(x=300,y=70,width=425,height=30)

        # input of mail subject
        GLineEdit_996=tk.Entry(root)
        GLineEdit_996["borderwidth"] = "3px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLineEdit_996["font"] = ft
        GLineEdit_996["fg"] = "#000000"
        GLineEdit_996["justify"] = "center"
        GLineEdit_996["text"] = "subject of mail"
        GLineEdit_996.place(x=270,y=225,width=450,height=30)

        #label
        GLabel_166=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_166["font"] = ft
        GLabel_166["fg"] = "#FFFFFF"
        GLabel_166["justify"] = "center"
        GLabel_166["text"] = "count"
        GLabel_166["background"] = "#357EC7"
        GLabel_166.place(x=824,y=460,width=150,height=45)

        #input of spam count
        GLineEdit_997=tk.Entry(root)
        GLineEdit_997["borderwidth"] = "3px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLineEdit_997["font"] = ft
        GLineEdit_997["fg"] = "#000000"
        GLineEdit_997["justify"] = "center"
        GLineEdit_997["text"] = "count"
        GLineEdit_997.place(x=824,y=500,width=450,height=30)

        #input of mail contents
        GLineEdit_566=tk.Text(root)
        GLineEdit_566["borderwidth"] = "3px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLineEdit_566["font"] = ft
        GLineEdit_566["fg"] = "#000000"
        GLineEdit_566.place(x=24,y=320,width=700,height=134)

        #showing the mail sent
        GLineEdit_567=tk.Text(root)
        GLineEdit_567["borderwidth"] = "3px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLineEdit_567["font"] = ft
        GLineEdit_567["fg"] = "#000000"
        GLineEdit_567.place(x=824,y=220,width=500,height=225)

        #input recievers list
        GLineEdit_156=tk.Entry(root)
        GLineEdit_156["borderwidth"] = "3px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLineEdit_156["font"] = ft
        GLineEdit_156["fg"] = "#000000"
        GLineEdit_156["justify"] = "center"
        GLineEdit_156["text"] = "exapmle1@gmail.com, example2@gmail.com, example3@gmail.com, .........................."
        GLineEdit_156.place(x=250,y=470,width=475,height=30)

        #button to attach files
        GButton_348=tk.Button(root)
        GButton_348["bg"] = "#DB59C8"
        GButton_348["borderwidth"] = "2px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GButton_348["font"] = ft
        GButton_348["fg"] = "#000000"
        GButton_348["justify"] = "center"
        GButton_348["text"] = "attach file"
        GButton_348.place(x=250,y=550,width=250,height=30)
        GButton_348["command"] = self.GButton_348_command

        #send button pro mode
        GButton_346=tk.Button(root)
        GButton_346["bg"] = "#4ADF4A"
        GButton_346["borderwidth"] = "2px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GButton_346["font"] = ft
        GButton_346["fg"] = "#000000"
        GButton_346["justify"] = "center"
        GButton_346["text"] = "Send in PRO Mode"
        GButton_346.place(x=150,y=630,width=205,height=50)
        GButton_346["command"] = self.GButton_346_command

        GButton_546=tk.Button(root)
        GButton_546["bg"] = "#EF4242"
        GButton_546["borderwidth"] = "2px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GButton_546["font"] = ft
        GButton_546["fg"] = "#000000"
        GButton_546["justify"] = "center"
        GButton_546["text"] = "Spam mails"
        GButton_546.place(x=900,y=535,width=205,height=50)
        GButton_546["command"] = self.GButton_546_command

        #send button slow mode
        GButton_345=tk.Button(root)
        GButton_345["bg"] = "#4ADF4A"
        GButton_345["borderwidth"] = "2px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GButton_345["font"] = ft
        GButton_345["fg"] = "#000000"
        GButton_345["justify"] = "center"
        GButton_345["text"] = "Send in SLOW Mode"
        GButton_345.place(x=450,y=630,width=205,height=50)
        GButton_345["command"] = self.GButton_345_command

        #network corner
        
        #know network
        GButton_1345=tk.Button(root)
        GButton_1345["bg"] = "#F04AB9"
        GButton_1345["borderwidth"] = "2px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GButton_1345["font"] = ft
        GButton_1345["fg"] = "#000000"
        GButton_1345["justify"] = "center"
        GButton_1345["text"] = "Know the network"
        GButton_1345.place(x=30,y=700,width=200,height=50)
        GButton_1345["command"] = self.GButton_1345_command

        #label
        GLabel_1696=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_1696["font"] = ft
        GLabel_1696["fg"] = "#000000"
        GLabel_1696["justify"] = "center"
        GLabel_1696["text"] = "public ip"
        GLabel_1696["background"] = "#F9E935"
        GLabel_1696.place(x=300,y=700,width=175,height=45)

        #label
        GLabel_1466=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_1466["font"] = ft
        GLabel_1466["fg"] = "#000000"
        GLabel_1466["justify"] = "center"
        GLabel_1466["text"] = "private ip"
        GLabel_1466["background"] = "#F9E935"
        GLabel_1466.place(x=500,y=700,width=175,height=45)

        #label
        GLabel_3166=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_3166["font"] = ft
        GLabel_3166["fg"] = "#000000"
        GLabel_3166["justify"] = "center"
        GLabel_3166["text"] = "mac"
        GLabel_3166["background"] = "#F9E935"
        GLabel_3166.place(x=700,y=700,width=175,height=45)


    def GButton_1345_command(self):
        # button to get data in network corner
        """
        clicking on the button will fill data in all labels in network corner
        """
        global GButton_1345,GLineEdit_156,GLabel_1696,GLabel_1466,GLabel_3166,GLineEdit_997,GLineEdit_567,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286
        hostname = socket.gethostname()
        private_ip_address = socket.gethostbyname(hostname)
        public_ip_address = get('https://api.ipify.org').text
        mac_data = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        GLabel_1696.config(text=str(public_ip_address))
        GLabel_1466.config(text=str(private_ip_address))
        GLabel_3166.config(text=str(mac_data))
        

    def GButton_345_command(self):
        global GLineEdit_156,GLabel_1696,GLabel_1466,GLabel_3166,GLineEdit_997,GLineEdit_567,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286
        global mail_id, mail_password, mail_subject, mail_body
        mail_id = GLineEdit_113.get()
        mail_password = GLineEdit_804.get()
        mail_subject = GLineEdit_996.get()
        mail_body = GLineEdit_566.get(1.0,"end-1c")[1:-2]
        recievers_list_from_box = GLineEdit_156.get()
        with open("mail_recievers.txt",'w') as rcvfile:
            rcvfile.write(recievers_list_from_box)
        with open("./mail_data.csv", "w") as csvfile:
            csvwriter  = writer(csvfile)
        with open("./mail_data.csv", "w") as csvfile:
            csvwriter  = writer(csvfile)
            csvwriter.writerow([mail_id,mail_password,mail_subject,mail_body])
        slow_mode_send_mails(writer = GLineEdit_567)

    def GButton_346_command(self):
        global GLineEdit_156,GLabel_1696,GLabel_1466,GLabel_3166,GLineEdit_997,GLineEdit_567,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286,mail_id, mail_password, mail_subject, mail_body
        mail_id = GLineEdit_113.get()
        mail_password = GLineEdit_804.get()
        mail_subject = GLineEdit_996.get()
        mail_body = GLineEdit_566.get(1.0,"end-1c")
        recievers_list_from_box = GLineEdit_156.get()
        with open("mail_recievers.txt",'w') as rcvfile:
            rcvfile.write(recievers_list_from_box)
        with open("./mail_data.csv", "w") as csvfile:
            csvwriter  = writer(csvfile)
        with open("./mail_data.csv", "w") as csvfile:
            csvwriter  = writer(csvfile)
            csvwriter.writerow([mail_id,mail_password,mail_subject,mail_body])
        pro_mode_send_mails(writer = GLineEdit_567)

    def GButton_348_command(self):
        global GLineEdit_156,GLabel_1696,GLabel_1466,GLabel_3166,GLineEdit_997,GLineEdit_567,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286
        get_file_from_windows()
        print("attach file button")

    def GButton_546_command(self):
        global GLineEdit_156,GLabel_1696,GLabel_1466,GLabel_3166,GLineEdit_997,GLineEdit_567,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286
        print("spammer started")
        spammer_code(GLineEdit_156.get(),int(GLineEdit_997.get()),writer = GLineEdit_567)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
