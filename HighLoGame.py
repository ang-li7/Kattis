import random

ans = int(random.random()*100)+1
guess = int(input("Enter your guess"))
numg = 1
while guess != ans:
    if guess>ans:
        print("Too high")
    else:
        print("Too low")
    numg = numg+1
    guess = int(input("Enter another guess"))

print("nice it took you "+str(numg)+"guesses")