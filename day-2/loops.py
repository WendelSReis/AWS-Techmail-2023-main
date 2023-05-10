"""
Loops While and For
Jogo da advinhacao
"""

# importar biblioteca que gerar numeros aleatorios
import random

# Exibir mensagem de boas-vindas
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# gerar numero aleatorio entre 1 - 10
number = random.randint(1,10)

# variavel de controle
isGuessRight = False

# Loop
while isGuessRight != True:
    # pedir ao usuario o numero
    guess = input("Guess a number between 1 and 10: ")
# condicional
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    # Enquanto o usuario nao advinhar
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
        

"""
Welcome to Guess the Number!
The rules are simple. I will think of a number, and you will try to guess it.
Guess a number between 1 and 10: 5
You guessed 5. Sorry, that isn’t it. Try again.
Guess a number between 1 and 10: 8
You guessed 8. That is correct! You win!
"""