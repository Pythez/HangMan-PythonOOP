'''
HangMan - Jonas van Raemdonck
0/12/2021 - start
1/12/2021 - working version with the option to enter your own word
'''

#Todo : catching errors

'''
Done: 
- new models
- Added functionality to use a chosen word
- Molding it into classes
'''

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
            file = open('Lists/programmingwords.csv', "r")
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                woorden.append(row)
            return woorden[0]

        elif self.keuze == 2:
            file = open('Lists/transportwords.csv', "r")
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                woorden.append(row)
            return woorden[0]

        elif self.keuze == 3:
            file = open('Lists/foodwords.csv', "r")
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                woorden.append(row)
                print(woorden[0])
            return woorden[0]

        elif self.keuze == 5:
            woord = input("What word do you want to play with?")
            woorden.append(woord)
            return woorden

        else:
            print("False input")


    def get_word(woorden):
        word = random.choice(woorden)
        return word.upper()


class Game():
    def __init__(self, id):
        self.id = 1

    def play(word):
        tries = 6
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        print("Welcome to hangman!")
        print(Game.display_hangman(tries))
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
                    print(guess + "is not the word.")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("Wrong guess.")
            print(Game.display_hangman(tries))
            print(word_completion)
            print("\n")
        if guessed:
            print("Congrats, you guessed the word! You won!")
        else:
            print("You ran out of tries. The word was " + word + " !")


    def display_hangman(tries):
        stages = [  # final state: head, torso, both arms, and both legs
                    """
                       --------
                       |/     |
                       |      O
                       |     \\|/
                       |      |
                       |\    / \\
                       --------
                    """,
                    # head, torso, both arms, and one leg
                    """
                       --------
                       |/     |
                       |      O
                       |     \\|/
                       |      |
                       |\    / 
                       --------
                    """,
                    # head, torso, and both arms
                    """
                       --------
                       |/     |
                       |      O
                       |     \\|/
                       |      |
                       |\     
                       --------
                    """,
                    # head, torso, and one arm
                    """
                       --------
                       |/     |
                       |      O
                       |     \\|
                       |      |
                       |\     
                       --------
                    """,
                    # head and torso
                    """
                       --------
                       |/     |
                       |      O
                       |      |
                       |      |
                       |\     
                       --------
                    """,
                    # head
                    """
                       --------
                       |/     |
                       |      O
                       |    
                       |      
                       |\     
                       --------
                    """,
                    # initial empty state
                    """
                       --------
                       |/     |
                       |      
                       |    
                       |      
                       |\     
                       -------- 
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
    game1 = Game(1)
    Game.play(CSV.get_word(woord))
    while input("Play Again? (Y/N) ").upper() == "Y":
        print('')
        print('')
        print('')
        main()


main()