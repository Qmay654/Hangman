import random


# making the hashed out version of word
def fakeword():
    guess = []

    for letter in realword:
        if letter == "-":
            guess.append("-")
        elif letter in corguess:
            guess.append(letter)
        elif letter in lets:
            guess.append('*')
    guessprint = (' '.join(map(str, guess)))
    print(guessprint)


while True:
    # making varibles
    lets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z'}
    corguess = []
    wrongguess = []
    points = 12
    corguessstr = ''

    # getting random word from document
    realword = (random.choice(list(open('Word.txt'))))

    # start of the game
    print(realword)
    while True:
        if wrongguess:
            print(str(wrongguess))
        print(str(points) + ' Life points left')
        fakeword()
        playerguess = input('Guess a letter or word: ')

        # win condition
        if playerguess == realword[0:-1]:
            print('You win! The correct word was ' + realword)
            break
        else:

            # wrong word guess
            if len(playerguess) > 1:
                print('That guess is not correct, you lose three points')
                points -= 3

                # lose time :(
                if points <= 0:
                    print('Sorry, you lose! The word was ' + realword)
                    break

            # correct letter guess
            elif len(playerguess) == 1:
                if playerguess in realword:
                    print('The letter was in the word')
                    corguess.append(playerguess)
                    corguessstr += playerguess

                    # win condition
                    if corguessstr == realword[0:-1]:
                        print('You win! The correct word was ' + realword)
                        break

                # wrong letter guess
                elif playerguess not in realword:
                    print('The letter was not in the word, you lose 1 point')
                    wrongguess.append(playerguess)
                    points -= 1

                    # lose time :(
                    if points <= 0:
                        print('Sorry, you lose! The word was ' + realword)
                        break

    # playing again
    again = input('Would you like to play again? ')
    if again == 'yes':
        t = 0
    elif again == 'sure':
        t = 0
    elif again == 'yes please':
        t = 0
    else:
        break
        
        
 
#12 Life points left
#* * * *
#Guess a letter or word: a
#The letter was not in the word, you lose 1 point
#['a']
#11 Life points left
#* * * *
#Guess a letter or word: c
#The letter was in the word
#['a']
#11 Life points left
#c * * *
#Guess a letter or word: e
#The letter was not in the word, you lose 1 point
#['a', 'e']
#10 Life points left
#c * * *
#Guess a letter or word: b
#The letter was not in the word, you lose 1 point
#['a', 'e', 'b']
#9 Life points left
#c * * *
#Guess a letter or word: h
#The letter was in the word
#['a', 'e', 'b']
#9 Life points left
#c h * *
#Guess a letter or word: n
#The letter was in the word
#['a', 'e', 'b']
#9 Life points left
#c h * n
#Guess a letter or word: i
#The letter was in the word
#['a', 'e', 'b']
#9 Life points left
#c h i n
#Guess a letter or word: chin
#You win! The correct word was chin

#Would you like to play again? no

#Process finished with exit code 0



