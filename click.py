# Button we click it and then it does stuff 
from tkinter import *

window = Tk()

window.title("click me")
def click():
    print("hello world")
button = Button(window,text="click me!!!")
button.config(command=click) # performs call back of function
button.config(font=("Ubuntu",50,"bold")
              ,background= "#ff6200",
              fg ="#fffb1f") 
button.config(activebackground="#ff0000",activeforeground="#fffb1f")
image = PhotoImage(file= "point_emoji.png")
image = image.subsample(5, 5)
button.config(image=image,compound="bottom")
            # this enable it to change background when you over on it to click.

button.pack() # it always allow each element to display
# putting in window that means the component we are adding the button to.

window.mainloop()
