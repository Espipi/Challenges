# import library
import random
from tkinter import *
from PIL import Image,ImageTk


window=Tk()
window.geometry("400x400")
window.title("Madlib app")

# Insert images
image=Image.open('image.png')
image.thumbnail((100,100),Image.ANTIALIAS)

photo=ImageTk.PhotoImage(image)
label_image=Label(image=photo).grid(row = 0, column = 1, columnspan=2, rowspan=1)

# display a welcome page
welcome = Label(window, text = "Welcome to Matlib Game", font=("times", 16, "bold")).grid(row = 2, column = 1, columnspan=2)

# Getting user input
#More funny

#e = tk.Entry(window, width=35, borderwidth=5)
#e.pack()
def enter_game():
    #funny_name= tk.Entry.get()
    #global name_of_player
    name_of_player = Entry(window, text = "Please provide fantasy game's name: ")
    name_of_player.get()
    #name_of_player.grid(row=0, column=0)
    #name_of_player=(funny_name)
    emoji_code = "\U0001F600"
    print(f"Hello {name_of_player}.get(){emoji_code}, welcome to madlib's game!!!")

# action of click

#mybutton = Button(window,tk.text = "Get me in", command = click)
l1= Label(window, text = "                     ").grid(row=4, column =0)
l1= Label(window, text = "Enter a funny name: ").grid(row=5, column =0)
e1 = Entry(window, font=("times", 10, "bold")).grid(row=5, column = 1)
btn= Button(window, text = "Get me in", command = enter_game).grid(row = 6, column = 1, columnspan= 1)



# Enter game





window.mainloop()