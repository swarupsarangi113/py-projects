#This is a guess the number game
import random
print('I am thinking of a number between 1 and 20')
secret_number = random.randint(1,20)

#print(secret_number)

attempts = int(input('How many guesses do you want? '))

for i in range(0,attempts) :
    guess = int(input('\nTake a guess. '))
    if guess < secret_number :
        print('Your guess is too low.')
    elif guess > secret_number :
        print('Your guess is too high.')
    else :
        break

if guess == secret_number :
    print('Good job! You guessed my number in ',i+1,' guesses!')
else :
    print('Nope. The number I was thinking of was',secret_number)

