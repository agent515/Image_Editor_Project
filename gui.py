import tkinter
from tkinter import *
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import image_editor as ie
from PIL import Image, ImageTk
# import time
import os
import webbrowser

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

        self.crop_button = Button(master, text="Crop",command= self.crop)
        self.crop_button.pack(side = LEFT, anchor = S)

        self.mirror_button = Button(master, text="Mirror",command= self.mirror)
        self.mirror_button.pack(side = LEFT, anchor = S)

        self.ioi_button = Button(master, text="Img over Img",command= self.pop)
        self.ioi_button.pack(side = LEFT, anchor = S)

        self.undo_button = Button(master, text= "Undo", command = self.undo)
        self.undo_button.pack(side = LEFT, anchor = S)

        self.redo_button = Button(master, text= "Redo", command = self.redo)
        self.redo_button.pack(side = LEFT, anchor = S)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side = LEFT, anchor = S)

        self.e_1 = Entry(master, textvariable = self.v, width = 40)
        self.e_1.pack(side = LEFT, anchor = S)

        self.e_2 = Entry(master, width = 30)
        self.e_2.pack(side = LEFT, anchor = S)

        self.Submit = Button(master, text = "Submit", command = self.get)
        self.Submit.pack(side = LEFT, anchor = S)

        # messagebox.showinfo("Utopia IE","Welcome!")
        menubar = Menu(master)
        master.config(menu=menubar)

        fileMenu = Menu(menubar)

        fileMenu.add_command(label="Open", command=self.open)
        fileMenu.add_command(label ="Save")
        ''', command = ie.save(self.img))'''
        fileMenu.add_command(label="Exit", command=master.quit)


        menubar.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menubar)

        editMenu.add_command(label = "Rotate", command = self.rotate)
        editMenu.add_command(label = "Mirror", command = self.mirror)
        editMenu.add_command(label = "Image over Image", command = self.pop)
        editMenu.add_command(label = "Resize", command = self.resize)
        editMenu.add_command(label = "Crop", command = self.crop)

        menubar.add_cascade(label = "Edit", menu=editMenu)
        helpMenu = Menu(menubar)
        helpMenu.add_command(label = "Help", command = self.help)
        #
        # helpMenu.add_cascade(label = "Help", menu = helpMenu)
        menubar.add_cascade(label="Help", menu=helpMenu)

    def open(self):
        # print("Enter file path:")
        # self.img = input()
        # print(self.img)
        self.choice = 1
        self.img = askopenfilename(filetypes = (("all files", "*.*"),("jpg image", ".jpg"),("jpeg image", ".jpeg"),("gif image", ".gif")), initialdir = "/home/rohit/Pictures")
        print(self.img)
        self.img = os.path.basename(self.img)
        #self.v.set("Enter file path: ")
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
        self.img2 = askopenfilename(filetypes = (("all files", "*.*"),("jpg image", ".jpg")), initialdir = "/home/rohit/Pictures")
        self.img2 = os.path.basename(self.img2)
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

        self.v.set("Enter the degree of ROTATION:")
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

    def undo(self):
        img = Image.open(self.prev)
        imge = ImageTk.PhotoImage(img)
        width, height = img.size
        self.canvas.create_image(0, 0,anchor = NW, image=imge)
        self.canvas.image = imge

    def redo(self):
        img = Image.open(self.img)
        imge = ImageTk.PhotoImage(img)
        width, height = img.size
        self.canvas.create_image(0, 0,anchor = NW, image=imge)
        self.canvas.image = imge

    def crop(self):
        self.choice = 7
        self.v.set("Enter dimensions (widthxheight): ")
        self.get()

    def help(self):
        webbrowser.open_new_tab("https://www.geeksforgeeks.org/working-images-python/")

    def get(self):
        self.input = self.e_2.get()

        if self.choice == 1:
            # print(self.img)
            # print(type(self.img))
            # print("self.get Executed")
            # self.img = self.input
            img = Image.open(self.img)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge
            ie.properties(self.img)
        elif self.choice == 2:

            # self.img2 = self.input
            # print(self.img2)
            self.prev = self.img
            self.mod = ie.picture_over_picture(self.img,self.img2)
            self.img = self.mod    #making the modified image the current self.img object of class MyFirstGUI
            img = Image.open(self.mod)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge
        elif self.choice == 3:

            self.v.set("Enter the degree of ROTATION:")
            self.degree = self.e_2.get()
            self.prev = self.img
            self.mod = ie.rotate(self.img,float(self.degree))
            print(self.mod)
            self.img = self.mod    #making the modified image the current self.img object of class MyFirstGUI
            img = Image.open(self.mod)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge
        elif self.choice == 4:
            self.prev = self.img
            self.mod = ie.resize(self.img)
            img = Image.open(self.mod)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge
        elif self.choice == 5:
            self.mod = ie.mirror(self.img)
            self.prev = self.img
            print(self.mod)
            img = Image.open(self.mod)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge
        elif self.choice == 6:
            self.undo()
        elif self.choice == 7:
            dim =self.input.split('x')
            width = dim[0]
            height = dim[-1]

            self.mod = ie.crop(self.img,int(width),int(height))
            self.prev = self.img
            print(self.mod)
            img = Image.open(self.mod)
            imge = ImageTk.PhotoImage(img)
            width, height = img.size
            self.canvas.create_image(0, 0,anchor = NW, image=imge)
            self.canvas.image = imge
        else:
            self.redo()

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
