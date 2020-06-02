'''
    LoginView :
    This view displays the login form.
'''
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import ttk
from controllers.AuthController import AuthController

class AuthView:

    master = None
    transfer_control_admin = None
    transfer_control_student = None

    def load(self):
        tab_control = ttk.Notebook(self.master)

        login_tab = Frame(tab_control,background="white",padx=20,pady=20)
        register_tab = Frame(tab_control,background="white",padx=20,pady=20)
        tab_control.add(login_tab, text='Login')
        tab_control.add(register_tab, text='Register')

        self.loginTab(login_tab)
        self.registerTab(register_tab)
        tab_control.pack(expand=1, fill='both')

    def loginTab(self,login_tab):
        # assign the frame
        frame = login_tab

        # create username input and label
        Label(frame, text="Username").grid(row=1, column=0)
        username_entry = Entry(frame, width=10)
        username_entry.grid(row=1, column=1)
        username_entry.focus()

        # create password input and label
        Label(frame, text="Password").grid(row=2, column=0)
        password_entry = Entry(frame,show="*", width=10)
        password_entry.grid(row=2, column=1)

        # login button
        Button(frame,   text="Login",padx=5,pady=5,
                command = lambda: self.loginControl(username_entry.get(),password_entry.get())
               ).grid(row=3, column=1,padx=10,pady=10)

        # save the entry fields names in the current object
        self.username_entry = username_entry
        self.password_entry = password_entry

    def registerTab(self,register_tab):
        # assign the frame
        frame = register_tab

        # create name input and label
        Label(frame, text="Name").grid(row=1, column=0)
        name_entry = Entry(frame, width=10)
        name_entry.grid(row=1, column=1)
        name_entry.focus()

        # create phone input and label
        Label(frame, text="Phone").grid(row=2, column=0)
        phone_entry = Entry(frame, width=10)
        phone_entry.grid(row=2, column=1)

        # create email input and label
        Label(frame, text="Email").grid(row=3, column=0)
        email_entry = Entry(frame, width=10)
        email_entry.grid(row=3, column=1)

        # create username input and label
        Label(frame, text="Username").grid(row=4, column=0)
        username_entry = Entry(frame, width=10)
        username_entry.grid(row=4, column=1)

        # create password input and label
        Label(frame, text="Password").grid(row=5, column=0)
        password_entry = Entry(frame, show="*", width=10)
        password_entry.grid(row=5, column=1)

        # create register button
        Button(frame, text="Register", padx=5, pady=5,
               command=lambda: self.registerControl(
                   name_entry.get(),phone_entry.get(),email_entry.get(),
                   username_entry.get(),password_entry.get())
               ).grid(row=6, column=1, padx=10, pady=10)

    def loginControl(self,username,password):
        ac = AuthController()
        status = ac.login(username,password)

        if status['code']:
            if status['role'] == 'admin':
                self.transfer_control_admin()
            else:
                self.transfer_control_student()
        else:
            message = status['message']
            messagebox.showwarning('Login Error',message)


    def registerControl(self,name,phone,email,username,password):
        ac = AuthController()
        status = ac.register(name,phone,email,username,password)

        if status['code']:
            messagebox.showinfo('Success',status['message'])
        else:
            messagebox.showerror('Error', status['message'])
