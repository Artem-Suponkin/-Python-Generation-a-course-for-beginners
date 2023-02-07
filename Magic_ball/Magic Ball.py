# Project description: magic ball 8 (the ball of fate) is a comic way to predict the future.
# The program should ask the user to ask a question in order to randomly answer it.
#
# Components of the project:
#
# Integers (int type);
# Variables;
# Data input/output (input() and print() functions);
# Conditional operator (if/elif/else);
# While loop;
# Infinite loop;
# Break, continue operators;
# Working with the random module to generate random numbers.

from random import *

answers = ['Indisputably', 'Predetermined', 'No doubt', 'Definitely yes', 'You can be sure of it', 'It seems to me - yes', 'Most likely', 'Good prospects', 'Signs say - yes', 'Yes', 'Its not clear yet, try again', 'Ask later', 'Its better not to tell', 'Its impossible to predict now', 'Concentrate and ask again', 'Dont even think', 'My answer is no', 'According to my data - no', 'Prospects are not very good', 'Very doubtful']

print('Hello World, I am a magic ball, and I know the answer to any of your questions.')
print("What's your name? ", end="")
print('Hello,', input() + '.')
flag = True

while flag == True:
    vop = input('Enter your question: ')
    print(choice(answers))
    ans = input('Do you want to ask another question? ')
    while True:
        if ans.lower() == 'yes':
            break
        elif ans.lower() == 'no':
            flag = False
            break
        else:
            print('Enter yes or no!!!')
            ans = input()
            continue

print('Come back if you have any questions!')