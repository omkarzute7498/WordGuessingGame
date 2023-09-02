import random

name = input("What Is Your Name? ")

print("All The Best !", name)

words = ['Smartphone', 'App', 'Bluetooth', 'Camera', 'Notification', 'Hotspot', 'Gaming', 'Charger', 'Call', 'Screen', 'Unlock', 'Payment']
word = random.choice(words)

print("Guess A Letter")

guesses = ''

turns = 12

while turns > 0:
    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")
        else:
            print("_")


            failed += 1

        if failed == 0:
            print("You Win")

            print("The Word Is: ", word)
            break

        print()
        guess = input("Guess A Letter:")

        guesses += guesses

        if guess not in word:

            turns -= 1

            print("Wrong")

            print("You Have ", +turns, "More Guesses Now")

            if turns == 0:
                print("You Loose")