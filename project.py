from tkinter import *
window = Tk() # intialize a window, and instance of a window 
window.geometry("420x420") # for size
window.title("First project")


image = PhotoImage(file="logo.png")
window.config(background="white") # is used when you want to make any change in your window

window.iconphoto(True,image)

# label = an area of the widget that holds text and/or an image within a window 
label = Label(window,text = "WELCOME",font= ("arial",20,"bold"),fg ="yellow" ,bg = "black",relief=RIDGE,bd=10,padx=10,pady=20) # x is left and right and y is up and dowm 
# image=image,compound="left" for image 
label.pack()
# label.place(x=0,y=0) to change the position of the font 
window.mainloop()#Place window on computer screen 



