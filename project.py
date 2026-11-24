from tkinter import *
window = Tk() # intialize a window, and instance of a window 
window.geometry("420x420") # for size
window.title("First project")


image = PhotoImage(file="logo.png")
window.config(background="white") # is used when you want to make any change in your window

window.iconphoto(True,image)
window.mainloop()#Place window on computer screen 

# label = an area of the widget that holds text and/or an image within a window 
label = Label(window,text = "WELCOME")
label.pack(window)



