import random

number = random.randint(1,99)



while True:
    guess = int(input("Guess the number (between 1 and 99): "))

    if guess == number :
        print('Congratulations, you guessed the number!')
        break
    if guess > number: 

        print('"Your guess is too high, try again.")')
        break
    else:
        print('"Your guess is too low, try again.")')
   