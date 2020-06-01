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

        login_tab = ttk.Frame(tab_control)
        register_tab = ttk.Frame(tab_control)
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
        Button(frame,   text="Login",
                command = lambda: self.loginControl(username_entry.get(),password_entry.get())
               ).grid(row=3, column=1)

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

        Label(frame, text="Password").grid(row=2, column=0)
        self.password_entry = Entry(frame, show="*", width=10)
        self.password_entry.grid(row=2, column=1)

        Button(frame, text="Login", command=self.loginControl).grid(row=3, column=1)

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


