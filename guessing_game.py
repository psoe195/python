"""
Guessing game between 1 and 100
if player's's guess is within 10, print getting close
if player's guess is more than 10, print getting far
"""

from random import randint

def input_next_move(max_num):
    valid_input = False
    while not valid_input:
        try:
            num = int(input('Enter your guess between 1 to {} : '.format(max_num)))
            if num >= 1 and num <= max_num:
                valid_input = True
            else:
                print('Invalid input. Please enter a number between 1 to {}'.format(max_num))
        except:
            print('Invalid input. Please enter numbers only between 1 to {}'.format(max_num))

    return num

max_num = 100
rand_num = randint(1, max_num)

# for your eyes only... uncomment for debugging purposes only
# otherwise you are cheating :-)
# print('{} is the random number you will need to guess'.format(rand_num))

still_guessing = True
num_try = 0
previous_guess = 0

while still_guessing:
    player_guess = input_next_move(max_num)

    # increment number of tries
    num_try += 1

    if player_guess == rand_num:
        print('Bravo!!!. The number is {} and you got it right in {} times'.format(rand_num, num_try))
        still_guessing = False
        break

    if num_try == 1 and abs(player_guess - rand_num) >= 10:
        print('COLD!')
    elif num_try == 1 and abs(player_guess - rand_num) < 10:
        print('WARM!')
    elif abs(player_guess - rand_num) < abs(previous_guess - rand_num):
        print('WARMER!!!')
    elif abs(player_guess - rand_num) >= abs(previous_guess - rand_num):
        print('COLDER!!!')

    previous_guess = player_guess

