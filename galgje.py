'''
HangMan - Jonas van Raemdonck
0/12/2021 - start
1/12/2021 - working version with the option to enter your own word
'''

#Todo : Adding functionality to choose words
#Todo : catching errors

import random
import csv

class CSV():
    def __init__(self, keuze):
        print("Class: csv activated!")
        self.keuze = keuze

    def woorden_ophalen(self):
        #Woordenlijst keuze of zelf ingegeven woord
        woorden = []

        if self.keuze == 1:
            file = open('programmingwoorden.csv', "r")
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                woorden.append(row)
            return woorden[0]

        elif self.keuze == 2:
            file = open('transportwoorden.csv', "r")
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                woorden.append(row)
            return woorden[0]

        elif self.keuze == 3:
            file = open('voedselwoorden.csv', "r")
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                woorden.append(row)
            return woorden[0]

        elif self.keuze == 5:
            woord = input("What word do you want to play with?")
            woorden.append(woord)
            return woorden[0]

        else:
            print("False input")

def get_word(woorden):
    word = random.choice(woorden)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word" + guess)
            elif guess != word:
                print(guess + "is the wrong word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():

    print("Met welke woordenlijst wil je spelen?")
    print("1) Programming woordenlijst")
    print("2) Transport woordenlijst")
    print("3) Voedsel woordenlijst")
    print("4) TBA")
    print("5) Zelf woord ingeven")
    while True:
        try:
            keuze = int(input('Mijn keuze: '))
            if keuze == 1 or 2 or 3 or 5:
                break
            else:
                main()
        except ValueError:
            print("Dat was geen valide getal.")
    csv1 = CSV(keuze)
    woord = CSV.woorden_ophalen(csv1)
    word = get_word(woord)
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        print('')
        print('')
        print('')
        main()


main()