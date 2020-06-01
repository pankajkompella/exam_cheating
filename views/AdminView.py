'''
    AuthView :
    This view displays the login form and registration form.
'''
import cv2
from tkinter import *
import tkinter.messagebox as messagebox
from PIL import ImageTk
from PIL import Image
import threading
import datetime
import os


class AdminView:

    master = None
    next = None
    count = 0
    image_label = None

    def load(self):
        self.frame = self.master
        self.outputPath = 'images'
        self.cascadePath = 'lib/nose.xml'

        self.title = Label(self.frame,text="Admin Detection", font=("Helvetica", 16),bg='#1289A7',foreground='white',padx=10,pady=10)
        self.title.grid(row=0,column=0,columnspan=3,pady=(0,10),sticky='nesw')

        self.b1 = Button(self.frame,text = "Start",command = self.startCamera,pady=10)
        self.b1.grid(row=2,column=0,sticky='nesw')

        self.b2 = Button(self.frame, text="Stop", command=self.stopCamera,pady=10)
        self.b2.grid(row=2,column=1,sticky='nesw')

        self.b3 = Button(self.frame, text="Capture", command=self.saveImage, pady=10)
        self.b3.grid(row=2, column=2,sticky='nesw')

        self.status = Label(self.frame, text="Status: -", font=("Helvetica", 12), bg='#cd6133', foreground='white',padx=10, pady=10)
        self.status.grid(row=3, column=0, columnspan=3, pady=(10, 0), sticky='nesw')




    def startCamera(self):

        p.set('stop', False)
        self.cascade = cv2.CascadeClassifier(self.cascadePath)
        self.cap = cv2.VideoCapture(0)

        self.t = threading.Thread(target=self.detection, args=(),daemon=True)
        self.t.start()
        message = "[STATUS] Camera Started"
        print(message)
        self.status.config(text=message)

    def detection(self):
        try:
            ret, image_frame = self.cap.read()
            image_frame = cv2.resize(image_frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            colorimage = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGB)
            grayimage = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
            nose_rects = self.cascade.detectMultiScale(grayimage, 1.7, 11)
            for (x, y, w, h) in nose_rects:
                y = int(y - 0.15 * h)
                cv2.rectangle(colorimage, (x, y), (x + w, y + h), (0, 255, 0), 3)

            self.img = Image.fromarray(colorimage)
            img = ImageTk.PhotoImage(self.img)

            if self.image_label is None:
                self.image_label = Label(self.frame,image=img, bg='silver')
                self.image_label.image = img
                self.image_label.grid(row=1, column=0, columnspan=3,pady=(0,10))
            # otherwise, simply update the panel
            else:
                self.image_label.configure(image=img)
                self.image_label.image = img

            if p.get('stop') != True:
                self.image_label.after(10, self.detection)
            else:
                self.image_label.image = None
                self.cap = None
        except:
            message = "[STATUS] Thread Halted"
            print(message)
            self.status.config(text=message)


    def stopCamera(self):
        p.set('stop',True)
        message = "[STATUS] Camera Stopped"
        print(message)
        self.status.config(text=message)



    def saveImage(self):
        ts = datetime.datetime.now()
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
        path = os.path.sep.join((self.outputPath, filename))

        # save the file
        if p.get('stop') != True:
            try:
                self.img.save(path)
                message = "[STATUS] saved image {}".format(filename)
                print(message)
                self.status.config(text=message)
            except AttributeError  as e:
                message = 'Camera not started'
                self.status.config(text=message)
                print(e)
            except FileNotFoundError as e:
                message = 'Output directory not found'
                self.status.config(text=message)
                print(e)

        else:
            messagebox.showinfo('Webcam Error','Start the camera to capture the image')
















