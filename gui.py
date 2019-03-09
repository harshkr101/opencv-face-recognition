import tkinter as tk
from tkinter import font  as tkfont
from PIL import Image, ImageTk
import mydb


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, LoginPage, SignupPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def enter_data(self, uname, email, password):
        mydb.enter_data(uname, email, password)
        frame = self.frames["LoginPage"]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        load = Image.open("new_logo.gif")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.pack()
        label2 = tk.Label(self, text="Welcome to face recognition system", font=controller.title_font)
        label2.pack()
        button = tk.Button(self, text="Next", command=lambda: controller.show_frame("LoginPage"))
        button.pack(side="bottom")


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login", font=controller.title_font)
        label.pack()
        uname_label = tk.Label(self, text="Username")
        uname_label.place(x=40, y=80)
        uname_entry = tk.Entry(self)
        uname_entry.place(x=200, y=80)
        pass_label = tk.Label(self, text="Password")
        pass_label.place(x=40, y=110)
        pass_entry = tk.Entry(self, show='*')
        pass_entry.place(x=200, y=110)
        login_button = tk.Button(self, text="Login")
        login_button.place(x=210, y=150)
        signup_button = tk.Button(self, text="SignUp", command=lambda: controller.show_frame("SignupPage"))
        signup_button.place(x=280, y=150)


class SignupPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="SignUp", font=controller.title_font)
        label.pack()
        uname = tk.StringVar()
        email = tk.StringVar()
        password = tk.StringVar()

        uname_label = tk.Label(self, text="Username")
        uname_label.place(x=40, y=80)
        uname_entry = tk.Entry(self, textvariable=uname)
        uname_entry.place(x=200, y=80)
        email_label = tk.Label(self, text="Email")
        email_label.place(x=40, y=110)
        email_entry = tk.Entry(self, textvariable=email)
        email_entry.place(x=200, y=110)
        pass_label = tk.Label(self, text="Password")
        pass_label.place(x=40, y=140)
        pass_entry = tk.Entry(self, show='*', textvariable=password)
        pass_entry.place(x=200, y=140)
        print(uname, email, password)
        signup_button = tk.Button(self, text="Submit", command=controller.enter_data(uname.get(), email.get(), password.get()))
        signup_button.place(x=200, y=170)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
