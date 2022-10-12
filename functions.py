from collections import namedtuple
from colorama import Fore
from numpy.random import randint
import time
from classes import *
import readchar

# -------------------------
# PSR 2022/2023 - Typing Test
#
# Work done by:
#
# Jorge Silva
# --------------------------

# Input data
Input = namedtuple('Input', ['requested', 'received', 'duration'])


def start():
    start_time = time.time()  # Number of seconds passed since January 1970

    return start_time


# Calculates the time passed since the start time
def end(start_time):
    end_time = time.time()
    duration_time = end_time - start_time
    return duration_time


def typing_test(use_time_mode, max_value):
    # Initialize
    inputs = []
    number_inputs = 0

    print(Fore.BLUE + '\nPress space bar to stop the test.\n' + Fore.RESET)

    # used_time_mode: chose time or input mode
    # max_value: max seconds in time mode or max input values in input mode
    if use_time_mode:
        try:  # Stops program when time runs out
            with Timeout(max_value):  # Class Timeout within max value
                while True:
                    # Random low case letter
                    low_case = randint(97, 122)
                    print('Type letter ' + Fore.BLUE + chr(low_case) + Fore.RESET)

                    # Get the key that was pressed and time of response
                    type_time_start = start()
                    key = readchar.readkey()
                    type_duration_time = end(type_time_start)

                    # Analyse the key to see if it's a space or not and stops the code if it is.
                    if key == str(' '):
                        print('\nYou pressed the space bar, test stopped.')
                        exit(0)

                    # Create tuple
                    input_namedtuple = Input(requested=chr(low_case), received=key,
                                             duration=round(type_duration_time, 3))
                    inputs.append(input_namedtuple)

                    # Check the random letter
                    if key == chr(low_case):
                        print('You typed the ' + Fore.GREEN + 'correct' + Fore.RESET + ' letter' + Fore.GREEN + key)
                    else:
                        print('You typed the ' + Fore.RED + 'incorrect' + Fore.RESET + ' letter' + Fore.RED + key)

        except Timeout.Timeout:
            pass

    else:
        while number_inputs < max_value:
            # Generate a random low case letter
            low_case = randint(97, 122)
            print('Type letter ' + Fore.BLUE + chr(low_case) + Fore.RESET)

            # Get time response from the pressed key
            type_time_start = start()
            key = readchar.readkey()
            type_duration_time = end(type_time_start)

            # If it is a space stops the code
            if key == str(' '):
                print(Fore.RED + 'You pressed the space bar, test aborted.\n')
                exit(0)

            # Create tuple
            input_namedtuple = Input(requested=chr(low_case), received=key,
                                     duration=round(type_duration_time, 3))
            inputs.append(input_namedtuple)

            # Check the random letter
            if key == chr(low_case):
                print('You typed the ' + Fore.GREEN + 'correct' + Fore.RESET + 'letter' + Fore.GREEN + key)
            else:
                print('You typed the ' + Fore.RED + 'incorrect' + Fore.RESET + 'letter' + Fore.RED + key)

            number_inputs += 1

    return inputs
