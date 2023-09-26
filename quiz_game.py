print("Welcome to my first program in python! This is a computer quiz.")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()

print("Ok! Let's start :)")
answer = input("What does CPU stand for?")
if answer == "central processing unit":
    print("Correct! ")
else: 
    print("Incorrect! The correct answer is central processing unit")

answer = input("")
if answer == "":
    print("Correct! ")
else: 
    print("Incorrect! ")