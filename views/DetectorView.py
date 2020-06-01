'''
    LoginView :
    This view displays the login form.
'''
import cv2
from tkinter import *
from PIL import ImageTk
from PIL import Image
import threading
import datetime
import os


class DetectorView:

    frame = None
    stop = False
    outputPath = 'images'
    cascadePath = 'lib/face.xml'

    def load(self):

        self.title = Label(self.frame,text="Exam Cheating Detection", font=("Helvetica", 16),bg='#1289A7',foreground='white',padx=10,pady=10)
        self.title.grid(row=0,column=0,columnspan=3,pady=(0,10),sticky='nesw')

        # Blank Image container to hold video frames
        img = Image.new('RGB', (500, 300), (255, 255, 255))
        img = ImageTk.PhotoImage(img)
        self.container = Label(self.frame, image=img, bg='silver')
        self.container.image = img
        self.container.grid(row=1, column=0, columnspan=3,pady=(0,10))

        self.b1 = Button(self.frame,text = "Start",command = self.startCamera,pady=10)
        self.b1.grid(row=2,column=0,sticky='nesw')

        self.b2 = Button(self.frame, text="Stop", command=self.stopCamera,pady=10)
        self.b2.grid(row=2,column=1,sticky='nesw')

        self.b3 = Button(self.frame, text="Capture", command=self.saveImage, pady=10)
        self.b3.grid(row=2, column=2,sticky='nesw')

        self.status = Label(self.frame, text="[Status] Click start button to run the webcamera", font=("Helvetica", 12), bg='#cd6133', foreground='white',padx=10, pady=10)
        self.status.grid(row=3, column=0, columnspan=3, pady=(10, 0), sticky='nesw')


    def startCamera(self):

        self.stop = False
        self.cascade = cv2.CascadeClassifier(self.cascadePath)
        self.cap = cv2.VideoCapture(0)

        self.t = threading.Thread(target=self.detection, args=(),daemon=True)
        self.t.start()
        self.printStatus("[STATUS] Camera Started")

    def detection(self):
        try:
            ret, image_frame = self.cap.read()
            image_frame = cv2.resize(image_frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            self.img = Image.fromarray(image_frame)

            colorimage = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGB)
            grayimage = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

            rects = self.cascade.detectMultiScale(grayimage, 1.7, 11)
            for (x, y, w, h) in rects:
                y = int(y - 0.15 * h)
                cv2.rectangle(colorimage, (x, y), (x + w, y + h), (0, 255, 0), 3)

            self.img = Image.fromarray(colorimage)
            img = ImageTk.PhotoImage(self.img)
            self.container.configure(image=img)
            self.container.image = img

            if self.stop != True:
                self.container.after(10, self.detection)
            else:
                self.container.image = None
                self.cap = None
        except:
            self.printStatus("[STATUS] Thread Halted")


    def stopCamera(self):
        self.stop = True
        self.printStatus("[STATUS] Camera Stopped")


    def saveImage(self):
        ts = datetime.datetime.now()
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
        path = os.path.sep.join((self.outputPath, filename))

        if self.stop != True:
            try:
                self.img.save(path)
                self.printStatus("[STATUS] saved image {}".format(filename))
            except:
                self.printStatus("[ERROR] Unable to save image")

        else:
            self.printStatus("[ERROR] Enable the camera to capture photo")

    def printStatus(self,message):
        self.status.config(text=message)
        print(message)














