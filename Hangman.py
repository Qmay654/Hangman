from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
import random


# Making hashed out version of the word
def fakeword():
    guesslist = []

    for letter in realword:
        if letter == "-":
            guesslist.append("-")
        elif letter in corguess:
            guesslist.append(letter)
        elif letter in lets:
            guesslist.append('_')
    guessprint = (' '.join(map(str, guesslist)))
    if "_" not in guesslist:
        textbox.insert(END, f"You Win! The word was " + realword + "\n")
        balloon = Label(root, width=0, image=balloons, bg="#800040")
        balloon.place(x=1250, y=0)
        playsound('C:/hangman/Horn.wav')
    text = Label(root, text=str(guessprint), padx=200, bg="#800040")
    text.config(font=("Courier", 54))
    text.grid(row=0, column=1)


# The meat of the game
def click():
    global img
    global image
    global health

    guess = entry.get()

    # Win
    if guess == realword[0:-1]:
        if health == 0:
            root.quit()
        for letter in guess:
            corguess.append(letter)
        fakeword()

    # Correct letter guess
    elif guess in realword:
        if health == 0:
            root.quit()
        textbox.insert(END, f"Your guess was " + guess + ", and it was in the word \n")
        corguess.append(guess)
        textbox.insert(END, str(health) + f" Health left \n")
        textbox.insert(END, f" \n")
    else:

        # If guess is bigger than 1
        if len(guess) > 1:
            textbox.insert(END, f"Your guess was " + guess + ", and it was not in the word \n")
            health -= 3
            if health < 0:
                lose()
            image += 3
            if image > 10:
                image = 9
        else:

            # If guess is only 1 long
            textbox.insert(END, f"Your guess was " + guess + ", and it was not in the word \n")
            health -= 1
            if health < 0:
                root.quit()
            image += 1
            wrong_let.append(guess)

        # Replacing the image
        img.pack_forget()
        img = Label(imageholder, image=hangmanlist[image + 1])
        img.pack()

        # Redefining the wrong letters
        wrong_area2 = Label(root, text='Wrong guesses are: ' + ' '.join(wrong_let), bg='#800040')
        wrong_area2.config(font=("Courier", 11))
        wrong_area2.grid(row=1, column=0)

        # Run out of health
        if health == 0:
            lose()
        else:
            textbox.insert(END, str(health) + f" Health left \n")
            textbox.insert(END, f" \n")

    fakeword()
    return


# Function for losing
def lose():
    global img
    for letter in realword:
        corguess.append(letter)
    fakeword()
    textbox.insert(END, str(health) + f" Health left \n")
    textbox.insert(END, f"Sorry, you lose! The word was " + str(realword) + "\n")
    textbox.insert(END, f"Press the enter or the exit button to quit the game\n")
    playsound('C:/hangman/sad.mp3')


def restart():
    global img
    global realword
    global health
    global corguess
    global wrong_let
    global image

    realword = (random.choice(list(open('C:/hangman/Word.txt'))))
    health = 10
    corguess = []
    wrong_let = []
    image = -1
    textbox.delete('1.0', END)
    textbox.insert(END, str(health) + f" Health left \n")
    textbox.insert(END, f"Enter your guess below \n")
    img.forget()
    img = Label(imageholder, image=hangman0)
    img.pack()
    wrong_area2 = Label(root, text='Wrong guesses are: ' + ' '.join(wrong_let), bg='#800040')
    wrong_area2.config(font=("Courier", 11))
    wrong_area2.grid(row=1, column=0)
    fakeword()


# Defining some variables
realword = (random.choice(list(open('C:/hangman/Word.txt'))))
health = 10
corguess = []
wrong_let = []
image = -1
lets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v',
        'w', 'x', 'y', 'z'}

# Setting up the window
root = Tk()
root.title("Hangman")
root.iconbitmap('C:/hangman/hangman.ico')
root.configure(bg="#800040")
root.geometry('1600x830')

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
balloons = ImageTk.PhotoImage(Image.open('C:/hangman/balloons.png'))

# Putting the images into a list
hangmanlist = [hangman0, hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7, hangman8, hangman9,
               hangman10]

# Putting a place for the images to be
imageholder = LabelFrame(root)
imageholder.grid(row=0, column=0)

# Putting the image into the image holder for the first time
img = Label(imageholder, image=hangman0)
img.pack()

# Making frame for scrollable text box
enterbox = Label(root, borderwidth=7)
enterbox.place(x=500, y=400)

# Making a scrollable text box
scrollbar = Scrollbar(enterbox)
scrollbar.pack(side=RIGHT, fill=Y)
textbox = Text(enterbox)
textbox.pack()
textbox.insert(END, str(health) + f" Health left \n")
textbox.insert(END, f"Enter your guess below \n")
# Attach textbox to scrollbar
textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)

# Area for inputting answer
entry = Entry(enterbox, width=105)
entry.pack()

# Button for inputting guess
button = Button(enterbox, text='Enter your guess', padx=273, command=click)
button.pack()

# Wrong letter area
wrong_area = Label(root, text='Wrong guesses are: ' + ' '.join(wrong_let), bg='#800040')
wrong_area.config(font=("Courier", 11))
wrong_area.grid(row=1, column=0)

# Quit button
button_quit = Button(root, text="Exit Game", command=root.quit)
button_quit.place(x=1500, y=800)

# Restart button
button_quit = Button(root, text="Restart", command=restart)
button_quit.place(x=1450, y=800)

fakeword()

root.mainloop()
