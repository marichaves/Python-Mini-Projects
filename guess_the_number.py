import random


n = random.randrange(-1, 11)
answer = input("Try to guess the number from 0 to 10: ")

print("My number for this turn was ", n)
if answer.lower() == n:
    print("Correct!")
   
else:
    print("You lost! :P")