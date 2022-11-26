import tkinter as tk
import tkinter.font as tkFont
from csv import *
from file_loader import *
from mass_mailer_pro_mode import pro_mode_send_mails
from mass_mailer_slow_mode import slow_mode_send_mails
data=None
GLineEdit_156,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286 = None,None,None,None,None,None,None,None,None,None,None
mail_id, mail_password, mail_subject, mail_body, recievers = "", "", "", """""", []

class App:
    def __init__(self, root):
        #setting title
        global GLineEdit_156,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286
        root.title("Mass mailer using python")
        root.configure(background="white")
        #setting window size
        width=1400
        height=720
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
        GLabel_560["background"]="black"
        GLabel_560.place(x=20,y=24,width=250,height=30)

        # label
        GLabel_268=tk.Label(root)
        GLabel_268["borderwidth"] = "5px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_268["font"] = ft
        GLabel_268["fg"] = "#FFFFFF"
        GLabel_268["justify"] = "center"
        GLabel_268["text"] = "Enter Application Password"
        GLabel_268["background"]="black"
        GLabel_268.place(x=24,y=72,width=250,height=30)

        # label
        GLabel_632=tk.Label(root)
        GLabel_632["borderwidth"] = "5px"
        ft = tkFont.Font(family='Arial',size=11,weight="bold")
        GLabel_632["font"] = ft
        GLabel_632["fg"] = "#F4A93F"
        GLabel_632["justify"] = "center"
        GLabel_632["text"] = "THE MASS MAILER PROJECT"
        GLabel_632["background"]="black"
        GLabel_632.place(x=24,y=150,width=700,height=40)

        # label
        GLabel_277=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_277["borderwidth"] = "5px"
        GLabel_277["font"] = ft
        GLabel_277["fg"] = "#FFFFFF"
        GLabel_277["justify"] = "center"
        GLabel_277["text"] = "Enter subject"
        GLabel_277["background"]="black"
        GLabel_277.place(x=24,y=225,width=200,height=30)

        # label
        GLabel_764=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_764["font"] = ft
        GLabel_764["fg"] = "#FFFFFF"
        GLabel_764["justify"] = "center"
        GLabel_764["text"] = "Enter Mail Content"
        GLabel_764["background"] = "black"
        GLabel_764.place(x=24,y=270,width=200,height=30)

        # label
        GLabel_286=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLabel_286["font"] = ft
        GLabel_286["fg"] = "#FFFFFF"
        GLabel_286["justify"] = "center"
        GLabel_286["text"] = "Enter recievers list"
        GLabel_286["background"] = "black"
        GLabel_286.place(x=24,y=470,width=200,height=30)

        # input of mail id
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

        # input of mail contents
        GLineEdit_566=tk.Text(root)
        GLineEdit_566["borderwidth"] = "3px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLineEdit_566["font"] = ft
        GLineEdit_566["fg"] = "#000000"
        GLineEdit_566.place(x=24,y=320,width=700,height=134)

        # input recievers list
        GLineEdit_156=tk.Entry(root)
        GLineEdit_156["borderwidth"] = "3px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GLineEdit_156["font"] = ft
        GLineEdit_156["fg"] = "#000000"
        GLineEdit_156["justify"] = "center"
        GLineEdit_156["text"] = "exapmle1@gmail.com, example2@gmail.com, example3@gmail.com, .........................."
        GLineEdit_156.place(x=250,y=470,width=475,height=30)

        # button to attach files
        GButton_348=tk.Button(root)
        GButton_348["bg"] = "#F9AB18"
        GButton_348["borderwidth"] = "2px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GButton_348["font"] = ft
        GButton_348["fg"] = "#000000"
        GButton_348["justify"] = "center"
        GButton_348["text"] = "attach file"
        GButton_348.place(x=250,y=550,width=250,height=30)
        GButton_348["command"] = self.GButton_348_command

        # send button pro mode
        GButton_346=tk.Button(root)
        GButton_346["bg"] = "#F9AB18"
        GButton_346["borderwidth"] = "2px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GButton_346["font"] = ft
        GButton_346["fg"] = "#000000"
        GButton_346["justify"] = "center"
        GButton_346["text"] = "Send in PRO Mode"
        GButton_346.place(x=150,y=630,width=205,height=50)
        GButton_346["command"] = self.GButton_346_command

        # send button slow mode
        GButton_345=tk.Button(root)
        GButton_345["bg"] = "#F9AB18"
        GButton_345["borderwidth"] = "2px"
        ft = tkFont.Font(family='Arial',size=12,weight="bold")
        GButton_345["font"] = ft
        GButton_345["fg"] = "#000000"
        GButton_345["justify"] = "center"
        GButton_345["text"] = "Send in SLOW Mode"
        GButton_345.place(x=450,y=630,width=205,height=50)
        GButton_345["command"] = self.GButton_345_command

    def GButton_345_command(self):
        global GLineEdit_156,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286
        global mail_id, mail_password, mail_subject, mail_body
        mail_id = GLineEdit_113.get()
        mail_password = GLineEdit_804.get()
        mail_subject = GLineEdit_996.get()
        mail_body = GLineEdit_566.get(1.0,"end-1c")
        recievers_list_from_box = GLineEdit_156.get().split(',')
        with open("mail_recievers.py",'w') as csvfile:
            csvwriter  = writer(csvfile)
            csvwriter.writerow([])
            csvwriter.writerow(recievers_list_from_box)
            csvwriter.writerow(",")
        with open("./mail_data.csv", "w") as csvfile:
            csvwriter  = writer(csvfile)
            csvwriter.writerow([])
        with open("./mail_data.csv", "w") as csvfile:
            csvwriter  = writer(csvfile)
            csvwriter.writerow([mail_id,mail_password,mail_subject,mail_body])
        slow_mode_send_mails()

    def GButton_346_command(self):
        global GLineEdit_156,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286,mail_id, mail_password, mail_subject, mail_body
        mail_id = GLineEdit_113.get()
        mail_password = GLineEdit_804.get()
        mail_subject = GLineEdit_996.get()
        mail_body = GLineEdit_566.get(1.0,"end-1c")
        recievers_list_from_box = GLineEdit_156.get().split(',')
        with open("mail_recievers.py",'w') as csvfile:
            csvwriter  = writer(csvfile)
            csvwriter.writerow([])
            csvwriter.writerow(recievers_list_from_box)
            csvwriter.writerow(",")
        with open("./mail_data.csv", "w") as csvfile:
            csvwriter  = writer(csvfile)
            csvwriter.writerow([])
        with open("./mail_data.csv", "w") as csvfile:
            csvwriter  = writer(csvfile)
            csvwriter.writerow([mail_id,mail_password,mail_subject,mail_body])
        pro_mode_send_mails()

    def GButton_348_command(self):
        global GLineEdit_156,GLineEdit_566,GLineEdit_996,GLineEdit_804,GLineEdit_113,GLabel_560,GLabel_268,GLabel_632,GLabel_277,GLabel_764,GLabel_286
        get_file_from_windows()
        print("attach file button")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
