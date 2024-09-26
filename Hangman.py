import random
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["tyraxl", "tyra", "derek", "charles", "angelo", "daniela", "meynard"]


def guessing():
    random_word = random.choice(word_list)

    blanks = "_" * len(random_word)
    print(blanks)

    life = 0
    gameover = False
    correct_letters = []

    while not gameover :

        display = ""

        print(hangman[life])

        user_input = input("Guess a letter: ").lower()
        if user_input in correct_letters:
            print("The letter already exist")

        for letter in random_word:
            if user_input == letter:
                display += letter
                correct_letters.append(user_input)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
        
        if user_input not in random_word:
            life += 1

        print(display)

        if "_" not in display:
            print("you win")
            gameover = True
        elif life == 6:
            print(hangman[life])
            print("you lose")
            gameover = True
        else:
            continue
        

guessing()
