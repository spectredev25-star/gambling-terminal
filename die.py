import random

def DieRoll():
    while True:
        print("Press 1 to roll the die.")
        print("Press 0 to exit.")
        try:
            roll = input("> ")
            roll = int(roll)
            if roll == 0:
                exit()
            elif roll == 1:
                random_roll = random.randint(1,6)
                print(f"🎲 You rolled a {random_roll}.")
                reset = input("Do you want to try again(y/n): ")
                if reset.lower() == "y":
                    continue
                elif reset.lower() == "n":
                    exit()
        except ValueError:
            print("👎Only digits are allowed.")
