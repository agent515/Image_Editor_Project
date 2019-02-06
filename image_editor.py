from PIL import Image

def properties(img):
    filename = "image.png"
    with Image.open(filename) as image:
        width, height = image.size
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

def picture_over_picture(name1,name2):
    try:
        #Relative Path
        #Image on which we want to paste
        img = Image.open(name1)

        #Relative Path
        #Image which we want to paste
        img2 = Image.open(name2)
        new_img = img.paste(img2, (50, 50))
        new = "new " + new_img
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
img = input("Enter image path: ")
print("Utopia provides various functioalities.. ")
n=0
while(n!=8):
    print("1.Open 2.Properties 3.Rotate 4.Resize 5.Mirror 6.Merge 7.Save 8.Exit")
    n=int(input("Enter your choice= "))
    if(n==1):
        Image.open(img)
    elif(n==2):
        properties(img)
    elif(n==3):
        rotate(img)
    elif(n==4):
        resize(img)
    elif(n==5):
        picture_over_picture(img)
    elif(n==6):
        mirror(img)
    elif(n==7):
        save(img)
    else:
        n=8
