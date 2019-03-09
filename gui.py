import tkinter as tk
from tkinter import font  as tkfont
from PIL import Image, ImageTk
import mydb


class SampleApp(tk.Tk):

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
        label=tk.Label(self,text="Login",font=controller.title_font)
        label.pack()
        uname_label=tk.Label(self,text="Username")
        uname_label.place(x=40,y=80)
        uname_entry=tk.Entry(self)
        uname_entry.place(x=200,y=80)
        pass_label = tk.Label(self, text="Password")
        pass_label.place(x=40, y=110)
        pass_entry = tk.Entry(self,show='*')
        pass_entry.place(x=200, y=110)
        login_button=tk.Button(self,text="Login")
        login_button.place(x=210,y=150)
        signup_button=tk.Button(self,text="SignUp")
        signup_button.pack(side="bottom")


class SignupPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
