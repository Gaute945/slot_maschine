from art import *
import random
import os
import subprocess
import time

#* function to check if input is a number
def is_number(value):
    if isinstance(value, str):
        return value.isdigit()
    return isinstance(value, (int, float))

#* delay for visual effects
delay = 2      

#* boot
tprint("Emoji_machine")

#* insert wallet
wallet = random_number = random.randint(1, 100)
#* input("Insert Valid Amount of coins ... ")
print("current wallet amount {}".format(wallet))

while True:
    #* bet amount
    spent = input("How Much To Bet one, two Or four. ")
    if spent in ["1", "2", "4"]:
        bool(True)
    else:
        exit()

    #* Convert the spent value to an integer
    spent = int(spent)

    if wallet > spent:
        wallet = wallet - spent
    else:
        print("Insufficient Funds. (Wallet Cannot Be Zero)")
        exit()

    #* spin
    spin1 = random_number = random.randint(1, 10)
    spin2 = random_number = random.randint(1, 10)
    spin3 = random_number = random.randint(1, 10)
    
    #* payout calculation
    if spin1 == 10:
        payout1 = spent * 3
    else:
        payout1 = 0
    if spin2 == 10:
        payout2 = spent * 3
    else:
        payout2 = 0
    if spin3 == 10:
        payout3 = spent * 3
    else:
        payout3 = 0
    
    #* show result (slots icons)
    time.sleep(1)
    if spin1 == 10:
        print("{}".format(spin1))
    else:
        print(spin1)
    time.sleep(2)
    if spin2 == 10:
        print("{}".format(spin2))
    else:
        print(spin2)
    time.sleep(3)
    if spin3 == 10:
        print("{}".format(spin3))
    else:
        print(spin3)

    #* payout
    payout = payout1 + payout2 + payout3
    
    if payout > 0:
        print("Your payout is ... ", end=" ")
        time.sleep(3)
        print("{}".format(payout))
    else:
        print("Your payout is ... ", end=" ")
        time.sleep(3)
        print(payout)
    
    wallet = payout + wallet

    #* show wallet
    print("current wallet amount {}".format(wallet))
    continue

"""
todo:
flashing colors
arcade sound
highscore for length
highscore for amount won
?jackpot
wallet can be zero but not negative
!
?
//
todo
*
"""