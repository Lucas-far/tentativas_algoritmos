

"""
Requirements
------------

resources      (type="module") to import variables and functions
sleep          (type="method") to set time delays between actions
"""

from resources import *
from time import sleep

input_algorithm_procedure: str = ''  # start()

input_countdown_pattern: int = 0     # get_countdown_pattern()

input_countdown_speed_rate: int = 0  # get_countdown_speed_rate()

input_initial_number: int = 0        # get_initial_number()

input_ending_number: int = 0         # get_ending_number()

option: int = 0                      # build_conditions_throw_result()
delays: tuple = ()                   # build_conditions_throw_result()

steps: tuple = ('',
                '1 - Should algorithm run?',
                '2 - Display of Instructions',
                '3 - Get countdown pattern',
                '4 - Get countdown speed rate',
                '5 - Get initial integer',
                '6 - Get ending integer',
                '7 - Execution of the countdown')

steps_colored: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n' for each_data in steps])


def start():
    """To ask if algorithm must or not run. If user provides (str) 'end': break. Else: continues."""

    global input_algorithm_procedure

    print(steps_colored[1])

    input_algorithm_procedure = input(doubt_run_algorithm)


def instructions():
    """To ask if algorithm must or not run. If user provides (str) 'end': break. Else: continues."""

    instructions_text: str = \
    f"""
    {steps_colored[2]}
    1. Provide countdown pattern
    2. Provide countdown speed rate
    3. Provide the initial number
    4. Provide the ultimate number
    5. The algorithm will perform a countdown based on provided pieces of information"""

    print(instructions_text)


def get_countdown_pattern():
    """To treat improper data while a proper integer number is not being provided."""

    global input_countdown_pattern

    input_text: str = \
    f"""
    {steps_colored[3]}
    {colors[0]}What countdown pattern do you choose?{colors[7]} 
    1. {click_arrow}
    Type 0 for ascending pattern    
    Type 1 for descending pattern
    2. {press_enter_key}
    -> """

    while True:
        try:
            input_countdown_pattern = int(input(input_text))
            while input_countdown_pattern < 0 or input_countdown_pattern > 1:  # while input = improper number
                error_input_integer_out_of_range(0, 1)                         # throw this error function
                get_countdown_pattern()                                        # repeat main function
            else:                                                              # otherwise
                break                                                          # go to the next step
        except ValueError:                                                     # except if input = wrong type
            error_input_integer_not_used(0, 1)                                 # then throw this error function, loop repeats


def get_countdown_speed_rate():
    """To treat improper data while a proper integer number is not being provided."""

    global input_countdown_speed_rate

    input_text: str = \
    f"""
    {steps_colored[4]}
    {colors[0]}What is the countdown speed rate?{colors[7]} 
    1. {click_arrow}
    Type [ 0 ] for speed rate: slow    
    Type [ 1 ] for speed rate: standard    
    Type [ 2 ] for speed rate: fast    
    Type [ 3 ] for speed rate: instant
    2. {press_enter_key}
    -> """

    while True:
        try:
            input_countdown_speed_rate = int(input(input_text))
            while input_countdown_speed_rate < 0 or input_countdown_speed_rate > 3:  # while input = improper number
                error_input_integer_out_of_range(0, 3)                               # throw this error function
                get_countdown_speed_rate()                                           # repeat main function
            else:                                                                    # otherwise
                break                                                                # go to the next step
        except ValueError:                                                           # except if input = wrong type
            error_input_integer_not_used(0, 3)                                       # then throw this error function, loop repeats


def get_initial_number():
    """To treat improper data while a proper integer number is not being provided."""

    global input_initial_number

    input_text: str = \
    f"""
    {steps_colored[5]}
    {colors[0]}What is the initial integer to begin the countdown?{colors[7]} 
    1. {click_arrow}
    2. Type any integer value
    3. {press_enter_key}
    -> """

    while True:
        try:
            input_initial_number = int(input(input_text))
            break
        except ValueError:                                 # if input = wrong type
            error_non_integer_input()                      # throw this error function, loop repeats


def get_ending_number():
    """To treat improper data while a proper integer number is not being provided."""

    global input_ending_number

    error_incorrect_ascending_order: str = \
    f"""
    {announcement}
    Initial number {colors[1]}must be smaller{colors[7]} than the ending number
    """

    error_incorrect_descending_order: str = \
    f"""
    {announcement}
    Initial number {colors[1]}must be bigger{colors[7]} than the ultimate number
    """

    input_text: str = \
    f"""
    {steps_colored[6]}
    {colors[0]}What is the ending integer to finish the countdown?{colors[7]} 
    1. {click_arrow}
    2. Type any integer value
    3. {press_enter_key}
    -> """

    while True:
        try:
            input_ending_number = int(input(input_text))

            if input_countdown_pattern == 0 and input_initial_number > input_ending_number:    # if incorrect ascending order
                print(error_incorrect_ascending_order)                                         # print this error function
                get_initial_number()                                                           # repeat previous function

            elif input_countdown_pattern == 1 and input_initial_number < input_ending_number:  # if incorrect descending order
                print(error_incorrect_descending_order)                                        # print this custom error
                get_initial_number()                                                           # repeat previous function

            else:                      # if correct order
                break                  # go to the next step
        except ValueError:             # except if input = wrong type
            error_non_integer_input()  # then throw this error function, loop repeats


def build_countdown_loop(start_number: int = 1, end_number: int = 10, skips: int = 1, delay: float = 1.0):
    """To custom countdown with a range based on the input numbers provided on the algorithm"""

    for each_index, each_data in enumerate(range(start_number, end_number, skips)):
        if each_index % 20:            # numbers will be printed in line, 20 by 20
            print(each_data, end=' ')  # argument end=' ' allows them to be printed in line
            sleep(delay)               # time lapse between each number printed
        else:                          # if the line has printed 20 numbers
            print('\n')                # break a line and start printing the next numbers
            print(each_data, end=' ')
            sleep(delay)

    print('\n')

    # ========== TUTORIAL ==========
    # ASSUMPTIONS:  start_number = 1 / end_number = 40 / skips = 1 / delay = 0.15

    # for each_index, each_data in enumerate(range(1, 10, 1))
    #    if each_index % 20:
    #        print(each_data, end='  ')
    #        sleep(0.15)
    #    else:
    #        print('\n')
    #        print(each_data, end='  ')
    #        sleep(0.15)

    # ========== RESULT ==========
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    # 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40


def build_conditions_throw_result():
    """To get and throw a result based on conditions, followed by a controlled inner loop"""

    global option, delays

    delays = (1.5, 1, 0.25, 0.0)

    # ========== TUTORIAL ========== (variable: option)
    # 1. It avoids the writing of many conditions
    # 2. It controls:
    #                - the inner while loop
    #                - the inner if
    #                - variable: delays (created above)

    # 3. It is compared to: input_countdown_speed_rate
    # 4. If they do not match, variable (option) will be increased until they do
    # 5. When they match, the countdown function is triggered and algorithm is restarted after it

    if input_countdown_pattern == 0:
        while option < 4:
            if input_countdown_speed_rate == option:
                print(steps_colored[7])
                # input_ending_number HAS TO BE SUM BY 1 IN ORDER TO REACH THE TARGET INPUT
                build_countdown_loop(input_initial_number, input_ending_number + 1, 1, delays[option])
                break
            else:
                option += 1
        option = 0

    elif input_countdown_pattern == 1:
        while option < 4:
            if input_countdown_speed_rate == option:
                print(steps_colored[7])
                # input_ending_number HAS TO BE SUBTRACTED BY 1 IN ORDER TO REACH THE TARGET INPUT
                build_countdown_loop(input_initial_number, input_ending_number - 1, -1, delays[option])
                break
            else:
                option += 1
        option = 0

    # ALTERNATIVE METHOD

    # if input_countdown_pattern == 0:
    #     if input_countdown_speed_rate == 0:
    #         create_countdown_loop(input_initial_number, input_ending_number, 1, 1, 0.30)

    #     elif input_countdown_speed_rate == 1:
    #         create_countdown_loop(input_initial_number, input_ending_number, 1, 1, 0.15)

    #     elif input_countdown_speed_rate == 2:
    #         create_countdown_loop(input_initial_number, input_ending_number, 1, 1, 0.05)

    #     elif input_countdown_speed_rate == 3:
    #         create_countdown_loop(input_initial_number, input_ending_number, 1, 1, 0)

    # elif input_countdown_pattern == 1:
    #     if input_countdown_speed_rate == 0:
    #         create_countdown_loop(input_initial_number, input_ending_number, -1, -1, 0.30)

    #     elif input_countdown_speed_rate == 1:
    #         create_countdown_loop(input_initial_number, input_ending_number, -1, -1, 0.15)

    #     elif input_countdown_speed_rate == 2:
    #         create_countdown_loop(input_initial_number, input_ending_number, -1, -1, 0.05)

    #     elif input_countdown_speed_rate == 3:
    #         create_countdown_loop(input_initial_number, input_ending_number, -1, -1, 0)


while True:
    welcome('Range of Numbers Exhibitor')
    start()
    if input_algorithm_procedure in algorithm_cease:  # if user provides 'end' = algorithm ceases
        print(closure)
        break
    instructions()
    get_countdown_pattern()
    get_countdown_speed_rate()
    get_initial_number()
    get_ending_number()
    build_conditions_throw_result()
