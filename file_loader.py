from tkinter import *
from tkinter import filedialog

filename = None
label_file_explorer = None
setter_flag = False

def browseFiles():
    global label_file_explorer,setter_flag
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
    setter_flag = True
    with open("attach_address.txt", 'w') as attachment_details_file:
        attachment_details_file.write(filename)
    print("file attached : ",filename)
    return filename

def browseFiles_2():
    global label_file_explorer,setter_flag
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
    setter_flag = True
    with open("attach_csv_address.txt", 'w') as attachment_details_file:
        attachment_details_file.write(filename)
    print("mails csv : ",filename)
    return filename

def get_file_from_windows(flag = 0):
    global label_file_explorer
    window = Tk()
    window.title('File Explorer')
    window.geometry("350x125")
    window.config(background = "white")
    label_file_explorer = Label(window,text = "Click Browse and select a file",width = 50, height = 4,fg = "gold", bg="black")
    if(flag == 1):
        button_explore = Button(window,text = "Browse Files",command = browseFiles_2,width= 50, height= 5, fg="black",bg="gold")
    else:
        button_explore = Button(window,text = "Browse Files",command = browseFiles,width= 50, height= 5, fg="black",bg="gold")
    label_file_explorer.grid(column = 1, row = 1)
    button_explore.grid(column = 1, row = 2)
    window.mainloop()
    if(setter_flag == True):
        return