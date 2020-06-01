
from tkinter import *
from views.DetectorView import DetectorView
from views.AdminView import AdminView
from views.AuthView import AuthView

class MyApp:

    master = None
    def run(self):
        self.window = Tk()
        self.window.title("My Application")
        self.login()
        self.window.mainloop()

    def login(self):
        self.loadMaster()
        av = AuthView()
        av.master = self.master
        av.transfer_control_admin = self.admin
        av.transfer_control_student = self.detector
        av.load()

    def detector(self):
        self.loadMaster()
        dv  = DetectorView()
        dv.master = self.master
        dv.next = self.admin
        dv.load()

    def admin(self):
        self.loadMaster()
        av = AdminView()
        av.master = self.master
        av.load()

    def loadMaster(self):

        if self.master != None:
            self.master.destroy()
        self.master = Frame(self.window, padx=10, pady=10)
        self.master.grid()

app = MyApp()
app.run()