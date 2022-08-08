import threading
from socket import *
from threading import *
from tkinter import *
from tkinter import messagebox


# Menu option , window information to the user
def New_Window():
    top = Toplevel()
    top.title("what do you need to know about us?")
    top.geometry("600x300")
    top.resizable(False, False)
    top.configure(bg="orange")
    aboutUsLbl = Label(top, font="Arial 12", fg="blue", bg="orange",
                       text="Hello and welcome to M Chat!, the most amazing to chat.\nFounded by Meshi Osmo Our goal is to"
                            " speak with fun and pleasure\nIn the most convenient and fast way thank you and I would love"
                            " to hear your opinion!(:")
    aboutUsLbl.place(x=0, y=0)


# window to send a feedback comment
class Contact():

    def __init__(self):
        self.top = Toplevel()
        self.top.title("Contact Us")
        self.top.geometry("500x500")
        self.top.resizable(False, False)
        self.top.configure(bg="orange")
        self.message_result = None

        ContactLbl = Label(self.top, text="Do you have a question/a problem? Contact us and we can help you! \n\n Mail:"
                                          "meshiosmo12@gmail.com \n Telephone:08-555-8789", fg="blue", bg="orange",
                           font="Arial 12")
        ContactLbl.place(x=0, y=0)

        ## Get feedback from user
        feedbackNameLbl = Label(self.top, text="Name:", fg="blue", bg="orange", font="Arial 12")
        feedbackNameLbl.place(x=0, y=65, )
        self.feedbackNameEnt = Entry(self.top, width=22, font="Arial 12")
        self.feedbackNameEnt.place(x=0, y=85)
        feedbackCommentLbl = Label(self.top, text="Comment:", fg="blue", bg="orange", font="Arial 12")
        feedbackCommentLbl.place(x=0, y=110)
        self.feedbackText = Text(self.top, width=30, height=10, font="Arial 10")
        self.feedbackText.place(x=0, y=130)
        sendBtn = Button(self.top, text="Send", fg="blue", bg="white", command=self.Send)
        sendBtn.place(x=0, y=295)
        clearBtn = Button(self.top, text="Clear", fg="blue", bg="white", command=self.Clear)
        clearBtn.place(x=40, y=295)

    def Send(self): # send mail
        print(f'Name: {self.feedbackNameEnt.get()}')
        print(f'Comment{self.feedbackText.get("1.0", END)}')
        self.Clear()
        messagebox.showinfo(title='Comments', message="Thanks for your comment!")

    def Clear(self): # Clear the fileds
        self.feedbackNameEnt.delete(0, END)
        self.feedbackText.delete("1.0", END)

# window to fill your details
class ChatWindow:
    def __init__(self):
        self.my_send_screen = Toplevel()
        self.my_send_screen.withdraw()

        self.userlog = Toplevel()
        self.userlog.title('User Login')
        self.userlog.geometry("500x500")
        self.userlog.resizable(False, False)
        self.userlog.configure(bg="orange")

        titleLbl = Label(self.userlog, text="Please login your name in to continue the chat!", font="Arial 16", bg="orange")
        titleLbl.place(x=15, y=25)

        NicknameLbl = Label(self.userlog, text="Name/Nickname:", font="Arial 14 bold", bg="orange")
        NicknameLbl.place(x=50, y=50)
        NicknameLblEnt = Entry(self.userlog, width=25, font=14)
        NicknameLblEnt.place(x=205, y=55)
        NicknameLblEnt.focus()

        genderLbl8 = Label(self.userlog, text="Gender:", font="Arial 14 bold", bg="orange", fg="black")
        genderLbl8.place(x=50, y=90)

        v = IntVar()
        radiobutton = Radiobutton(self.userlog, text="Female",
                                  variable=v,
                                  padx=20,
                                  value=1, font=("Arial", 12), bg="orange",
                                  compound='center')
        radiobutton.place(x=110, y=115)

        radiobutton2 = Radiobutton(self.userlog, text="Male",
                                   variable=v,
                                   padx=25,
                                   value=2, font=("Arial", 12), bg="orange",
                                   compound='center')
        radiobutton2.place(x=125, y=135)

        radiobutton3 = Radiobutton(self.userlog, text="Other",
                                   variable=v,
                                   padx=30,
                                   value=3, font=("Arial", 12), bg="orange",
                                   compound='center')
        radiobutton3.place(x=135, y=155)

        # befor you enter the chat , make sure that your details are fully filled in
        loginbBtn = Button(self.userlog, text="Login", font="Arial 14 bold", command=lambda: self.continue_chat(NicknameLblEnt.get()))
        loginbBtn.place(x=180, y=205)

        self.userlog.mainloop()
       # function move to the chat window
    def continue_chat(self, name):
        self.userlog.destroy()
        self.go_chat(name)
        self.my_send_screen.mainloop()


    # The window chat function
    def go_chat(self, name):
        self.name = name
        self.my_send_screen.deiconify()
        self.my_send_screen.title("ChatRoom")
        self.my_send_screen.resizable(False, False)
        self.my_send_screen.configure(width=470, height=550, bg="white")
        # user name in the chat
        nameLbl = Label(self.my_send_screen, bg="white", fg="orange", text=self.name, font="Arial 12", pady=5)
        nameLbl.place(x=400, y=10)

        ## textBox Chat
        self.message_result = Text(self.my_send_screen, width=50, height=50)
        self.message_result.place(x=0, y=0)

        # lable background
        buttomBackgroundLbl = Label(self.my_send_screen, bg="light blue", height=80)
        buttomBackgroundLbl.place(relwidth=1, rely=0.830)
        # The entry widget to send message to server , make sure to write first your name to connection the chat
        self.entMsg = Entry(self.my_send_screen, bg="white", fg="black", font="Arial 12")
        self.entMsg.place(relwidth=1, relheight=0.08, rely=0.830, relx=0.0012)
        self.entMsg.focus()
        # send button for sending messages
        btnMsg = Button(self.my_send_screen, text="Send", font="Arial 10 bold", width=15, bg="orange",fg="white", command=self.sendMessage)
        btnMsg.place(relwidth=1, rely=0.900)
        self.message_result.config(cursor="arrow")
        threading.Thread(target=self.receive_message).start()
        Thread.daemon = True


    # function the server send to the client
    def receive_message(self):
        while True:
            try:
             self.server_message = client.recv(2048).decode()
             print(self.server_message)
             self.message_result.insert(END,"\n" +"Server:" + self.server_message)
            except:
               print("An Error")
    #function the client send to the server
    def sendMessage(self):
            self.message = self.entMsg.get()
            self.message_result.insert(END,"\n"+"You:"+self.message)
            client.send(self.message.encode(FORMAT))



FORMAT = "utf-8"


client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1",4468))

# the main window when you run the program
window = Tk()
window.title('M Chat')
window.geometry("700x700")
window.resizable(False, False)
window.configure(bg='orange')

lbl1 = Label(window, text="Welcome to M Chat!\n", font=("Arial", 28), bg="orange", fg="white")
lbl1.place(x=190, y=205)
lbl2 = Label(window, text="Amazing to chat.", font=("Arial", 20), bg="orange", fg="white")
lbl2.place(x=240, y=265)
btn1 = Button(window, text="Next", font=("Arial", 12), bg="white", fg="red", command=ChatWindow)
btn1.place(x=320, y=325)

# The Menu widget
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label="Contact", command=Contact)
new_item.add_command(label="About us", command=New_Window)
new_item.add_separator()
new_item.add_command(label='Exit', command=exit)
menu.add_cascade(label='Menu', menu=new_item)
window.config(menu=menu)
window.mainloop()
