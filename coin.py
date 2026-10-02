import random

def CoinFlip():
    while True:
        print("Press 1 to flip the coin.")
        print("Press 0 to exit.")
        try:
            flip = input("> ")
            flip = int(flip)
            if flip == 0:
                exit()
            elif flip == 1:
                random_flip = random.randint(0,1)
            if random_flip == 0:
                print("🤯 You flipped a head.")
                reset = input("Do you want to try again(y/n): ")
                if reset.lower() == "y":
                    num_of_trys = 3
                elif reset.lower == "n":
                    exit()
            else:
                print("😢 You flipped a tail.")
                reset = input("Do you want to try again(y/n): ")
                if reset.lower() == "y":
                    continue
                elif reset.lower() == "n":
                    exit()
        except ValueError:
            print("👎Only digits are allowed.")
