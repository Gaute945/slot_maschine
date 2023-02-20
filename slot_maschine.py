import os
import random
import subprocess
import time

from art import *

"""
todo:
//colors
arcade sound
*highscore for length
highscore for amount won
database for amount house has won
?jackpot
"""

# * function to check if input is a number
def is_number(value):
    if isinstance(value, str):
        return value.isdigit()
    return isinstance(value, (int, float))


# * delay for visual effects
delay = 2

# * boot
print("\033[40m")
print("\033[33m")
tprint("Emoji_machine")
print("\033[0m")

# * insert wallet
wallet = random_number = random.randint(1, 100)
# * input("Insert Valid Amount of coins ... ")
print("\033[43m wallet amount {}\033[0m".format(wallet))
rounds = 0
score = 0

while True:
    # * bet amount
    spent = input(
        "Bet \033[41m one \033[0m, \033[43m two \033[0m Or \033[42m four \033[0m. "
    )
    if spent in ["1", "2", "4"]:
        bool(True)
    else:
        exit()

    # * Convert the spent value to an integer
    spent = int(spent)

    #* adjust balance
    if wallet > spent:
        wallet = wallet - spent
    else:
        print(" \033[31m Insufficient funds (Wallet Cannot Be Zero) \033[0m")
        print("Try to beat round {}!".format(rounds))
        exit()

    # * spin
    spin1 = random_number = random.randint(1, 10)
    spin2 = random_number = random.randint(1, 10)
    spin3 = random_number = random.randint(1, 10)
    # * round/score count
    rounds += 1
    # * payout calculation
    if spin1 == 10:
        payout1 = spent * 3
        payout1 + score
    else:
        payout1 = 0
    if spin2 == 10:
        payout2 = spent * 4
        payout2 + score
    else:
        payout2 = 0
    if spin3 == 10:
        payout3 = spent * 5
        payout3 + score
    else:
        payout3 = 0

    # * show result (slots icons)
    time.sleep(1)
    if spin1 == 10:
        print("\u001b[32m{}\u001b[0m".format(spin1))
    else:
        print(spin1)
    time.sleep(2)
    if spin2 == 10:
        print("\u001b[32m{}\u001b[0m".format(spin2))
    else:
        print(spin2)
    time.sleep(3)
    if spin3 == 10:
        print("\u001b[32m{}\u001b[0m".format(spin3))
    else:
        print(spin3)

    # * payout
    payout = payout1 + payout2 + payout3

    if payout > 0:
        print("Payout is ... ", end=" ")
        time.sleep(3)
        print("\u001b[32m{}\u001b[0m".format(payout))
    else:
        pass

    wallet = payout + wallet

    # * show wallet
    time.sleep(delay)
    print("Current wallet amount \u001b[32m{}\u001b[0m".format(wallet))
    #* round counter
    print("Round \u001b[32m{}\u001b[0m".format(rounds))
    #* highscore score
    print("Highscore \u001b[32m{}\u001b[0m".format(score))
    time.sleep(delay)