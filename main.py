
from colors import Colors
welcome_msg = f'''
    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    |{Colors.Gold}SPCTRE'S GAMBLING TERMINAL{Colors.RESET}|
    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    ⚡SYSTEM STATUS : ACTIVE
'''

command_msg = f'''
    {Colors.Gold}Select Game{Colors.RESET}
    {Colors.YELLOW}(1).{Colors.RESET} 🎯 Number Guess
    {Colors.YELLOW}(2).{Colors.RESET} 🎲 Dice Roll
    {Colors.YELLOW}(3).{Colors.RESET} 💰 Coin Flip
    {Colors.YELLOW}(4).{Colors.RESET} ❌ Exit
    '''

def main():
    print(welcome_msg)
    while True:
        print(command_msg)
        try:
            command = input("> ")
            command = int(command)
            if command == 1:
                from number_guess import NumGuess
                NumGuess()
            elif command == 2:
                from die import DieRoll
                DieRoll()
            elif command == 3:
                from coin import CoinFlip
                CoinFlip()
            elif command == 4:
                exit()
        except ValueError:
            print("👎Only digits are allowed.")

if __name__ == "__main__":
    main()