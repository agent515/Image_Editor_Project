import tkinter
from tkinter import *
import image_editor as ie
from PIL import Image, ImageTk
import time

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("UTOPIA IE")

        self.v = StringVar()
        self.v.set("Intructions will be mentioned here.")
        self.label = Label(master, text="WELCOME TO THE UTOPIA IMAGE EDITOR")
        self.label.pack()

        self.canvas = Canvas(self.master, width = 1500, height = 700)
        self.canvas.pack(side = TOP)
        self.canvas.place(x = 5, y = 20)

        self.open_button = Button(master, text="Open", command= self.open )
        self.open_button.pack(side = LEFT, anchor = S)

        self.rotate_button = Button(master, text="Rotate",command= self.rotate)
        self.rotate_button.pack(side = LEFT, anchor = S)

        self.resize_button = Button(master, text="Resize",command= self.resize)
        self.resize_button.pack(side = LEFT, anchor = S)

        self.mirror_button = Button(master, text="Mirror",command= self.mirror)
        self.mirror_button.pack(side = LEFT, anchor = S)

        self.ioi_button = Button(master, text="Img over Img",command= self.pop)
        self.ioi_button.pack(side = LEFT, anchor = S)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side = LEFT, anchor = S)

        self.e_1 = Entry(master, textvariable = self.v, width = 40)
        self.e_1.pack(side = LEFT, anchor = S)

        self.e_2 = Entry(master, width = 30)
        self.e_2.pack(side = LEFT, anchor = S)

        self.Submit = Button(master, text = "Submit", command = self.get)
        self.Submit.pack(side = LEFT, anchor = S)

    def open(self):
        # print("Enter file path:")
        # self.img = input()
        # print(self.img)
        self.choice = 1
        self.v.set("Enter file path: ")
        # time.sleep(10)
        # self.v.set("")

        # self.get()
        # canvas = Canvas(self.master, width = 200, height = 200)
        # canvas.pack(side = BOTTOM)
        # img = Image.open(self.img)
        # imge = ImageTk.PhotoImage(img)
        # width, height = img.size
        # self.canvas.create_image(0, 0,anchor = NW, image=imge)
        # self.canvas.image = imge
        # ie.properties(self.img)


    def pop(self):
        self.choice = 2
        self.v.set("Enter file path of the other image:")
        # print("Enter file path of the other image:")
        # self.img2 = input()
        # self.mod = ie.picture_over_picture(self.img,self.img2)
        # img = Image.open(self.mod)
        # imge = ImageTk.PhotoImage(img)
        # width, height = img.size
        # self.canvas.create_image(0, 0,anchor = NW, image=imge)
        # self.canvas.image = imge

    def rotate(self):
        self.choice = 3

        # self.v.set("Enter the degree of ROTATION:")
        # self.degree = self.e_2.get()
        # self.mod = ie.rotate(self.img,float(self.degree))
        # img = Image.open(self.mod)
        # imge = ImageTk.PhotoImage(img)
        # width, height = img.size
        # self.canvas.create_image(0, 0,anchor = NW, image=imge)
        # self.canvas.image = imge


    def resize(self):
        self.choice = 4
        # self.mod = ie.resize(self.img)
        # img = Image.open(self.mod)
        # imge = ImageTk.PhotoImage(img)
        # width, height = img.size
        # self.canvas.create_image(0, 0,anchor = NW, image=imge)
        # self.canvas.image = imge

    def mirror(self):
        self.choice = 5
        self.get()
        # self.mod = ie.mirror(self.img)
        # img = Image.open(self.mod)
        # imge = ImageTk.PhotoImage(img)
        # width, height = img.size
        # self.canvas.create_image(0, 0,anchor = NW, image=imge)
        # self.canvas.image = imge

    def get(self):
        self.input = self.e_2.get()

        if self.choice == 1:
            # print(self.img)
            # print(type(self.img))
            # print("self.get Executed")
            self.img = self.input
            img = Image.open(self.img)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge
            ie.properties(self.img)
        elif self.choice == 2:

            self.img2 = self.input
            print(self.img2)
            self.mod = ie.picture_over_picture(self.img,self.img2)
            img = Image.open(self.mod)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge
        elif self.choice == 3:
            self.v.set("Enter the degree of ROTATION:")
            self.degree = self.e_2.get()
            self.mod = ie.rotate(self.img,float(self.degree))
            img = Image.open(self.mod)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge
        elif self.choice == 4:
            self.mod = ie.resize(self.img)
            img = Image.open(self.mod)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge
        else:
            self.mod = ie.mirror(self.img)
            img = Image.open(self.mod)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge

        # print(self.img)
        # print(type(self.img))
        # print("self.get Executed")
        # img = Image.open(self.img)
        # imge = ImageTk.PhotoImage(img)
        # width, height = img.size
        # self.canvas.create_image(0, 0,anchor = NW, image=imge)
        # self.canvas.image = imge
        # ie.properties(self.img)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
