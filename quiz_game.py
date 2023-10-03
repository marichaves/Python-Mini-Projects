print("Welcome to my first program in python! This is a computer quiz.")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()

print("Ok! Let's start :)")
score = 0  # Initialize the player's score

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is central processing unit")

# Question 2
answer = input("What is RAM short for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is random access memory")

# Question 3
answer = input("What is the primary function of an operating system? ")
if answer.lower() == "to manage hardware and software resources":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is to manage hardware and software resources")

# Question 4
answer = input("What does GPU stand for in the context of computers? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is graphics processing unit")

# Question 5
answer = input("What is the purpose of a firewall in computer security? ")
if answer.lower() == "to protect a network from unauthorized access":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is to protect a network from unauthorized access")

# Display the final score
print(f"Your final score is: {score} out of 5")