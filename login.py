import tkinter as tk
from tkinter import font as tkfont

import sqlite3

# make db connection
dbname = "face_db"
conn = sqlite3.connect(dbname)
c = conn.cursor()


def enter_data(name, email, passwd):
    statement = 'INSERT INTO LOGIN VALUES("{n}","{e}","{password}")'.format(n=name, e=email, password=passwd)
    conn.execute(statement)
    print("Data: ", name, email, passwd)
    print("Writing successful")
    conn.commit()


class Login(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, LoginPage, SignupPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        logo = tk.PhotoImage(file="")
        image_label = tk.Label(self, image=logo)
        image_label.pack(anchor=tk.N)
        label = tk.Label(self, text="Welcome to face recognition system", font=controller.title_font)
        label.pack()
        button1 = tk.Button(self, text="Next", command=lambda: controller.show_frame("LoginPage"))
        button1.pack()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login Page")
        label.pack(side="top")
        login_label = tk.Label(self, text="Enter Name :")
        login_label.pack(anchor=tk.W)
        login_entry = tk.Entry(self)
        login_entry.pack(anchor=tk.NW)
        pass_label = tk.Label(self, text="Enter Password :")
        pass_label.pack(anchor=tk.NW)
        pass_entry = tk.Entry(self, show="*")
        pass_entry.pack(anchor=tk.NW)
        button = tk.Button(self, text="Login", command=lambda: controller.show_frame("StartPage"))
        button.pack(side="left")
        button2 = tk.Button(self, text="SignUp", command=lambda: controller.show_frame("SignupPage"))
        button2.pack(side="left")


class SignupPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="SignUp Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        name_label = tk.Label(self, text="Enter Name:")
        name_label.place(x=30, y=50)
        name_entry = tk.Entry(self)
        name_entry.place(x=130, y=50)

        email_label = tk.Label(self, text="Enter E-mail:")
        email_label.place(x=30, y=80)
        email_entry = tk.Entry(self)
        email_entry.place(x=130, y=80)

        passwd_label = tk.Label(self, text="Enter Password:")
        passwd_label.place(x=30, y=110)
        passwd_entry = tk.Entry(self, show="*")
        passwd_entry.place(x=130, y=110)

        # get data from the forms
        name = str(name_entry.get())
        email = str(email_entry.get())
        password = str(passwd_entry.get())

        print("Data: ", name, email, password)
        button = tk.Button(self, text="Submit",command=lambda : enter_data(name,email,password))
        button.place(x=150, y=150)
        button2 = tk.Button(self, text="LoginPage", command=lambda: controller.show_frame("LoginPage"))
        button2.place(x=50, y=150)


if __name__ == "__main__":
    app = Login()
    app.mainloop()
    conn.close()
