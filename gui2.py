# import modules

from tkinter import *
import os
import mydb
from PIL import ImageTk, Image


# Designing window for registration


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global email
    global username_entry
    global password_entry
    global email_entry

    username = StringVar()
    password = StringVar()
    email = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.place(x=40, y=40)
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.place(x=120, y=40)
    password_lable = Label(register_screen, text="Password * ")
    password_lable.place(x=40, y=80)
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.place(x=120, y=80)
    email_label = Label(register_screen, text="Email *")
    email_label.place(x=40, y=120)
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.place(x=120, y=120)
    Button(register_screen, text="Register", width=10, height=1, command=register_user).place(x=150, y=150)


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").place(x=40, y=40)
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.place(x=120, y=40)
    Label(login_screen, text="Password * ").place(x=40, y=80)
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.place(x=120, y=80)
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).place(x=80, y=150)
    Button(login_screen, text="Register", width=10, height=1, command=register).place(x=180, y=150)


def selection():
    global selection_screen
    selection_screen = Toplevel(main_screen)
    selection_screen.geometry("300x250")
    selection_screen.title("Make your Selection")
    Label(selection_screen, text="Recognise Face in :", font="14").pack(anchor=W)
    rb_value = IntVar()
    Radiobutton(selection_screen, text="Image File", variable=rb_value, value=1).pack(anchor=W)
    Radiobutton(selection_screen, text="Video Stream", variable=rb_value, value=2).pack(anchor=W)
    rbvalue = int(rb_value.get())
    print(rbvalue)
    btn = Button(selection_screen, text="Next")
    btn.pack()
    if rbvalue == 1:
        btn.config(command=select_image_file())
        print("Select image")
    elif rbvalue == 2:
        btn.config(command=launch_video_file())
        print("launch video")
    else:
        pass


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    registration_success = mydb.enter_data(str(username_info), str(email_info), str(password_info))
    print(registration_success)

    if registration_success:
        register_success()
    else:
        register_failed()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)


# Implementing event on login button

def login_verify():
    login_check = mydb.check_login(str(username_verify.get()), str(password_verify.get()))

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if login_check:

        login_success()

    else:

        login_failed()


# Designing popup for login success


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Successful login ")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


def login_failed():
    global login_failed_screen
    login_failed_screen = Toplevel(login_screen)
    login_failed_screen.title("Failed")
    Label(login_failed_screen, text="Login Failed. Check your credentials or enter data into fields").pack()
    Button(login_failed_screen, text="OK", command=delete_login_failed).pack()


def launch_video_file():
    os.system(
        "python video_recognizer.py -d face_detection_model -m openface_nn4.small2.v1.t7 -r output/recognizer.pickle -l output/le.pickle ")


def select_image_file():
    pass


def register_success():
    global register_success_screen
    register_success_screen = Toplevel(login_screen)
    register_success_screen.title("Successful ")
    register_success_screen.geometry("150x100")
    Label(register_success_screen, text="Registration Successful").pack()
    Button(register_success_screen, text="OK", command=delete_register_success).pack()


def register_failed():
    global register_failed_screen
    register_failed_screen = Toplevel(login_screen)
    register_failed_screen.title("Failed")
    Label(register_failed_screen,
          text="Registration  Failed. Enter data into all fields or Username already present").pack()
    Button(register_failed_screen, text="OK", command=delete_register_failed).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    selection()


def delete_login_failed():
    login_failed_screen.destroy()


def delete_login_screen():
    login_screen.destroy()


def delete_register_success():
    register_success_screen.destroy()


def delete_register_failed():
    register_failed_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.title("Welcome")
    load = Image.open("new_logo.gif")
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.pack()
    button = Button(text="Next", command=login)
    button.pack(anchor=SE)
    mainloop()


main_account_screen()
