from tkinter import *
from PIL import ImageTk, Image

# Setting up the window
root = Tk()
root.title("Hangman")
root.iconbitmap('C:/Hangman/hangman.ico')
root.configure(bg="grey")
root.geometry("1500x800")

# Getting the images
hangman0 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman0.png'))
hangman1 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman1.png'))
hangman2 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman2.png'))
hangman3 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman3.png'))
hangman4 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman4.png'))
hangman5 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman5.png'))
hangman6 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman6.png'))
hangman7 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman7.png'))
hangman8 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman8.png'))
hangman9 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman9.png'))
hangman10 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman10.png'))

# Putting the images into a list
hangmanlist = [hangman0, hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7, hangman8, hangman9,
               hangman10]

# Putting a place for the images to be
imageholder = LabelFrame(root)
imageholder.grid(row=0, column=0)

# Putting the image into the image holder for the first time
img = Label(imageholder, image=hangman0)
img.pack()

# Making the text for the first time
text = Label(root, text='_ _ _ _ _', padx=400, bg="grey")
text.config(font=("Courier", 54))
text.grid(row=0, column=1)

# Making frame for scrollable text box
enterbox = LabelFrame(root)
enterbox.size()
enterbox.grid(row=1, column=1)

# Making a scrollable text box
scrollbar = Scrollbar(enterbox)
scrollbar.pack(side=RIGHT, fill=Y)
textbox = Text(enterbox)
textbox.pack()
for i in range(10):
    textbox.insert(END, f"This is an example line {i}\n")
# attach textbox to scrollbar
textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)

# Button for inputting guess
button = Button(enterbox, text='Enter your guess')
button.pack()

root.mainloop()
