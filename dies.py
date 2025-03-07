import tkinter as tk
from PIL import Image,ImageTk
import random

window = tk.Tk()
window.geometry("1000x500")
window.title("Dice Roll")

dice = ["Project6/dice1.jpeg","Project6/dice2.jpeg","Project6/dice3.jpeg","Project6/dice4.jpeg","Project6/dice5.jpeg","Project6/dice6.jpeg"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x = 40 , y = 100)
label2.place(x = 800 , y = 100)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    label2.image = image2

button = tk.Button(window,text='ROLL' , bg='black' ,font='Times 20 bold' , fg='white' , command=dice_roll)
button.place(x = 600 , y = 20)
window.mainloop()

