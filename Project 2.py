import random
##Guess the number:
max = input("Enter in a positive integer for the maximum range for your guessing game: ") #range of guess
answer = random.randrange(int(max)) + 1 #random guess for 1 to max of range.
print("Let's play a game. Try and guess a number between 1 and " + max)
guess = int(input("Your guess: "))
tries = 1 #tracks how many attempts it took
while guess != answer:
    print("Try again")
    tries += 1
    if guess < answer:
        print("A little higher")
        guess = int(input("Your new guess:"))
    elif guess > answer:
        print("A little lower")
        guess = int(input("Your new guess:"))

print("Nice job! The answer was " + str(answer))
print("It took you " + str(tries) +" times!")