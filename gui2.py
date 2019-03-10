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
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    email_label = Label(register_screen, text="Email *")
    email_label.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()


# Designing window for login

def login():
    main_screen.wm_minsize()
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    Button(login_screen, text="Register", width=10, height=1, command=register).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    registration_success = mydb.enter_data(str(username_info), str(email_info), str(password_info))
    l1 = Label(register_screen, text="", font=("calibri", 11))
    l1.pack()
    if registration_success:
        l1.config(text="Registration Success", fg="green")
    else:
        l1.config(text="Invalid Entry", fg="red")

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)


# Implementing event on login button

def login_verify():
    login_check = mydb.check_login(str(username_verify.get()), str(password_verify.get()))

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if login_check:

        login_sucess()

    else:

        login_failed()


# Designing popup for login success


def login_sucess():
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


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_login_failed():
    login_failed_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def delete_login_screen():
    login_screen.destroy()


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
