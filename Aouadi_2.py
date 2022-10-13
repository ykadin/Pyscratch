import random

"""Computer statements"""
ss = "Lets play guess the number"
dq = "Pick a difficulty level: (1, 2, or 3): "
sq = "I have my number, whats your guess?"
chances = 0
print(ss)
level = input(dq)
if level > "3":
    print("Invalid input")
    chances = 0
else:

    while chances < 8:

        if level == "1":
            num = random.randint(1, 10)
            user = int(input(sq))
            if user == num:
                print(f"You got it in {chances + 1} tries!")
            elif user > num:
                print("Too high. Guess again:")
            elif user < num:
                print("Too low. Guess again:")
            elif user != num:
                print("Invalid Input.")
            else:
                print("Try again!")
            chances += 1

        if level == "2":
            num = random.randint(1, 100)
            user = int(input(sq))
            if user == num:
                print(f"You got it in {chances + 1} tries!")
            elif user > num:
                print("Too high. Guess again:")
            elif user < num:
                print("Too low. Guess again:")
            elif user != num:
                print("Invalid Input.")
            else:
                print("Try again!")
            chances += 1

        if level == "3":
            num = random.randint(1, 1000)
            user = int(input(sq))
            if user == num:
                print(f"You got it in {chances + 1} tries!")
            elif user > num:
                print("Too high. Guess again:")
            elif user < num:
                print("Too low. Guess again:")
            elif user != num:
                print("Invalid Input.")
            else:
                print("Try again!")
            chances += 1

    if chances == 8:
        close = input("You lost, play again? (y)es or (n)o)")
        if close == 'y' or 'Y':
            chances = 0
        elif close == 'N' or 'n':
            print("Goodbye!")
    else:
        print("Invalid input.")
