import tkinter
from tkinter import *
import image_editor as ie

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("UTOPIA IE")

        self.label = Label(master, text="WELCOME TO THE UTOPIA IMAGE EDITOR")
        self.label.pack()

        self.open_button = Button(master, text="Open", command= self.open)
        self.open_button.pack()

        self.rotate_button = Button(master, text="Rotate",command= self.rotate)
        self.rotate_button.pack()

        self.resize_button = Button(master, text="Resize",command= self.resize)
        self.resize_button.pack()

        self.mirror_button = Button(master, text="Mirror",command= self.mirror)
        self.mirror_button.pack()

        self.ioi_button = Button(master, text="Img over Img",command= self.pop)
        self.ioi_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def open(self):
        print("Enter file path:")
        self.img = input()
        ie.properties(self.img)

    def pop(self):
        print("Enter file path of the other image:")
        self.img2 = input()
        ie.picture_over_picture(self.img,self.img2)


    def rotate(self):
        ie.rotate(self.img)

    def resize(self):
        ie.resize(self.img)

    def mirror(self):
        ie.mirror(self.img)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
