# Importing random module to get random number
import random

# Importing math module to perform logarithm operations
import math

lowerBound = int(input("Enter the lower bound:- "))

upperBound = int(input("Enter the upper bound:- "))

print(f"\n\t You have {round(math.log((upperBound - lowerBound + 1),2))} chances to guess the correct number")

number = random.randint(lowerBound,upperBound)

# Initializing count to zero
count = 0

while count < math.log((upperBound - lowerBound + 1),2):
    
    count += 1
    
    guess = int(input("Enter the number you guessed:- "))
    
    if number == guess:
        print(f"\n\tCongratulations you have guessed the right number in {count} times")
        break
    elif number > guess:
        print("\n\tYou have guessed too smaller number!")
    elif number < guess:
        print("\n\tYou have guessed too greater number")
if count >= math.log((upperBound - lowerBound + 1),2):
    print("\tThe number is %d" %number)
    print("\tBetter Luck next time!")
        
    