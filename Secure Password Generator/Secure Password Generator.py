#Project description: the program generates a set number of passwords and includes a smart setting for the length of the password, 
#as well as which characters need to be included in it and which ones to exclude.
#
#Components of the project:
#
#Integers (int type);
#Variables;
#Data input/output (input() and print() functions);
#Conditional operator (if/elif/else);
#For loop;
#Writing custom functions;
#Working with the random module to generate random numbers.

import random

digits = '0123456789'
lowercase_letters = 'acdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ""

#защита от дурака да нет
def da(a):
    while a.lower() != 'yes' and a.lower() != "no":
        a = input("Invalid input, enter yes or no \n")
    if a.lower() == "yes":
        return True

#сама функция
def generate_password(s):
    for i in range(int(n)):
        password = random.sample(s, int(lenght))
        print("".join(password))

print("""Good afternoon! "Smart Password" generates a set number of passwords and includes a smart setting for the length of the password,
as well as which characters need to be included in it and which ones to exclude. \n""")
n = input('Enter the number of passwords to generate \n')
while n.isdigit() == False:
    n = input("Incorrect input, enter a number \n")
lenght = input('Enter the length of one password \n')
while lenght.isdigit() == False:
    lenght = input("Incorrect input, enter a number \n")
cifr = input('Should I include numbers? Enter "yes" or "no"\n')
if da(cifr):
    chars += digits
lower = input('Should I include uppercase letters? Enter "yes" or "no"\n')
if da(lower):
    chars += lowercase_letters
upper = input('Should I include lowercase letters? Enter "yes" or "no"\n')
if da(upper):
    chars += uppercase_letters
punctu = input('Should punctuation be included? Enter "yes" or "no"\n')
if da(punctu):
    chars += punctuation
neodn = input('Should the ambiguous characters "il1Lo0O" be excluded? Enter "yes" or "no"\n')
if da(neodn):
   for c in "il1Lo0O":
        chars = chars.replace(c, "")

generate_password(chars)
