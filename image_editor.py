from PIL import Image


def properties(path):
    filename = "image.png"
    img = Image.open(path)
    width, height = img.size
    print("Width = "+str(width)+" Height = "+str(height))
        #Image.size gives a 2-tuple and the width, height can be obtained

def save(img):
    img.save(path, format)
    # format is optional, if no format is specified,
    #it is determined from the filename extension

def rotate(name):
    try:
        #Relative Path
        img = Image.open(name)
        print("THE IMAGE ROTATION")
        angle = float(input("Degree: "))
        #Angle given
        img = img.rotate(angle)
        new = "new " + name
        #Saved in the same relative location
        img.save(new)
    except IOError:
        pass

def resize(name):
    try:
         #Relative Path
        img = Image.open("name")
        width, height = img.size

        img = img.resize((width/2, height/2))

        #Saved in the same relative location
        new = "new " + name
        img.save(new)
    except IOError:
        pass

def picture_over_picture(name1):
    try:
        #Relative Path
        #Image on which we want to paste
        img = Image.open(name1)

        name2 = input("Enter path of image 2: ")
        #Relative Path
        #Image which we want to paste
        img2 = Image.open(name2)
        new_img = img.paste(img2, (50, 50))
        new = "new " + name1
        #Saved in the same relative location
        img.save(new)

    except IOError:
        pass

def mirror(name):
    try:
        #Relative Path
        img = Image.open(name)

        #transposing image
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        #Save transposed image
        transposed_img.save("transposed.jpg")
    except IOError:
        pass



print("Welcome To Utopia Image Editor!")
path = input("Enter image path: ")
print("Utopia provides various functioalities.. ")
n=0
while(n!=8):
    print("1.Open 2.Properties 3.Rotate 4.Resize 5.Mirror 6.Merge 7.Save 8.Exit")
    n=int(input("Enter your choice= "))
    if(n==1):
        img = Image.open(path)
        print("Opened")
    elif(n==2):
        properties(path)
    elif(n==3):
        rotate(path)
    elif(n==4):
        resize(path)
    elif(n==5):
        picture_over_picture(path)
    elif(n==6):
        mirror(path)
    elif(n==7):
        save(path)
    else:
        n=8
