import random

def NumGuess():
    num_of_trys = 3
    score = 0
    while True:
        if num_of_trys > 0:
            secret_num = random.randint(1,10)
            print("🔐 Target Locked...")
            print("🧠 Can you guess the secret number (1-10)")
            try:
                prompt = input("Enter your guess: ")
                prompt = int(prompt)
                num_of_trys -= 1
                if prompt == secret_num:
                    print(f"🔮You are such a good gambler! You wre made for this!!")
                    score +=1
                    reset = input("Do you want to try again(y/n): ")
                    if reset.lower() == "y":
                        num_of_trys = 3
                    elif reset.lower == "n":
                        exit()
                elif prompt > secret_num:
                    print("\t📡ANALYZING GUESS...")
                    print("💡Secret Number is Lower")
                    print(f"\t♥ATTEMPTS REMAINING: {num_of_trys}.")
                    continue
                elif prompt < secret_num:
                    print("\t📡ANALYZING GUESS...")
                    print("💡Secret Number is Higher")
                    print(f"\t♥ATTEMPTS REMAINING: {num_of_trys}.")
                    continue
            except ValueError:
                print("🚩Secret number is a digit not letter")
        else:
            print("💔You have exhausted your trials.")
            print(f"\n\t📢Your total score is {score}")
            reset = input("Do you want to try again(y/n): ")
            if reset.lower() == "y":
                num_of_trys = 3
            elif reset.lower() == "n":
                exit()
