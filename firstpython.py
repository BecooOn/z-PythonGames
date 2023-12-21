import tkinter as tk
import random
answer = random.randint(0,100)

question = 'What number am I thinking of? Enter the between 0-100: '
print ("Let's play the guessing game!")
right = int(input('How many rights do you want to have? Enter it! : '))
temp = right

while 100 > right > 0:
    guess = int(input(question))
    right -= 1
    if guess < answer:
        print('Little higher! CAUTION: {} out of {} guesses left.' .format(right, temp))
    elif guess > answer:
        print('Little lower! CAUTION: {} out of {} guesses left.' .format(right, temp))
    else:
        print(f'Answer is: {answer}')
        print('Are you a MINDREADER!!!')
        print('Your grade is: ', (100 - (temp-right)*(100/temp)))
        break
if guess != answer:
  print('You don\'t have any right to guess! Game over!')
  print(f'Answer was: {answer}')
  print('Your grade is: ', (100 - (temp-right)*(100/temp)))