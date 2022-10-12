import argparse
from colorama import Fore, Style
from collections import namedtuple
from readchar import readkey
from time import sleep, time, ctime
import time
from pprint import pprint
import pprint
from classes import *
from functions import *
from statistics import mean


# -------------------------
# PSR 2022/2023 - Typing Test
#
# Work done by:
#
# Jorge Silva
# --------------------------

def main():
    # Give arguments
    parser = argparse.ArgumentParser(add_help=False,
                                     description='Definition of ' + Fore.BLUE + 'test' + Style.RESET_ALL + ' mode')
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='show ' + Fore.BLUE + 'help' + Style.RESET_ALL + ' message and' + Fore.BLUE + ' exit' + Style.RESET_ALL)
    parser.add_argument('-utm', '--use_time_mode', action='store_const', const=True, default=False,
                        help='Max number of seconds ' + Fore.RED + 'for time' + Fore.RESET + ' mode or maximum number '
                                                                                             'of inputs ' + Fore.RED
                             + 'for' + Fore.RESET + ' number of inputs mode')
    parser.add_argument('-mv', '--max_value', type=int, default=5,
                        help='Max number of seconds ' + Fore.RED + 'for time' + Fore.RESET + ' mode or maximum number '
                                                                                             'of inputs ' + Fore.RED
                             + 'for' + Fore.RESET + ' number of inputs mode')

    args = vars(parser.parse_args())

    # Print information about the mode and the keys to press
    print(args)
    print(Fore.BLUE + 'PSR 2022/23' + Style.RESET_ALL + ' Typing Test')

    if args['use_time_mode']:
        print('Time Mode Active. You have ' + Fore.RED + str(args['max_value']) +
              Fore.RESET + ' seconds to finish.')
    else:
        print('Maximum Number Activate. You have' + Fore.RED + str(args['max_value']) +
              Fore.RESET + ' inputs available to finish.')
        print("\nPress any key to start the the test.\n")

    # Waiting for a key to start the code
    readchar.readkey()
    # Start counting
    start_time = start()

    # Initialize stats and start date of the test
    stats = {'test_start': ctime()}

    # Call function for each mode
    if args['use_time_mode']:
        inputs = typing_test(use_time_mode=True, max_value=args['max_value'])
    else:
        inputs = typing_test(use_time_mode=False, max_value=args['max_value'])

    test_duration_time = end(start_time)
    print('\n You finished the test. These are your stats: \n')

    # Durations
    type_average_durations = [input_namedtuple.duration for input_namedtuple in inputs]
    type_hit_average_durations = [input_namedtuple.duration for input_namedtuple in inputs
                                  if input_namedtuple.requested == input_namedtuple.received]
    type_miss_average_durations = [input_namedtuple.duration for input_namedtuple in inputs
                                   if input_namedtuple.requested != input_namedtuple.received]

    # Additional stats.
    stats['test_end'] = ctime()
    stats['number_of_types'] = len(type_average_durations)
    stats['number_of_hits'] = len(type_hit_average_durations)
    stats['number_of_misses'] = len(type_miss_average_durations)

    if bool(inputs):
        stats['accuracy'] = round(len(type_hit_average_durations) / len(type_average_durations), 3)
    else:
        stats['accuracy'] = None

    stats['test_duration'] = round(test_duration_time, 3)
    stats['inputs'] = inputs

    if bool(inputs):
        stats['type_average_duration'] = round(mean(type_average_durations), 3)
    else:
        stats['type_average_duration'] = None
    if bool(type_hit_average_durations):
        stats['type_hit_average_duration'] = round(mean(type_hit_average_durations), 3)
    else:
        stats['type_hit_average_duration'] = None
    if bool(type_miss_average_durations):
        stats['type_miss_average_duration'] = round(mean(type_miss_average_durations), 3)
    else:
        stats['type_miss_average_duration'] = None

    # Print all information about stats
    pprint.pprint(stats)

    if bool(inputs):
        if stats['accuracy'] == 1:
            print('It was Accurate')
        elif stats['accuracy'] == 0:
            print('It was not Accurate')


if __name__ == '__main__':
    main()
