

"""
Requirements
------------

1. resources ->                -> module to import variables and functions
2. datetime  -> datetime.now() -> method to get current complete date and time at this moment
"""

from widgets import *
from datetime import date

input_algorithm_start: str = ''
input_birth_year: int = 0
current_year = date.today().year
current_age: int = 0
grown_up_age = 18
enrollment_year: int = 0

# Variables to inform
steps: tuple = ('', '1 - Should algorithm run? ', '2 - Display of Instructions', '3 - Provide input: year of birth',
                '4 - Display of result')

steps_colored: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n' for each_data in steps])

def start():
    """ To ask if algorithm must or not run. It will continue if any key besides 'n' is chosen """

    global input_algorithm_start
    print(steps_colored[1])
    input_algorithm_start = input(should_algorithm_run())

def instructions():
    """ To print procedures of the algorithm. """

    instructions_text = f"""
    {steps_colored[2]}
    1 - First input: provide your birth year
    2 - It will be checked if your age is suitable or not to enroll to the army
    """
    print(instructions_text)
    input(instruction)  # to prevent next content scrolling...

def get_birth_year():
    """ To treat improper data while a proper integer number is not being provided. """

    global input_birth_year

    input_text = f"""
    {steps_colored[3]}
    {colors[0]}What is your birth year?{colors[7]} 
    1. {click_arrow}
    2. Type your birth year
    3. {press_enter_key}
    -> """

    while True:
        try:
            input_birth_year = int(input(input_text))
            while input_birth_year <= 0 or input_birth_year > 9999:  # while input = improper number
                error_input_integer_out_of_range(0, 9999)            # throw this error function
                get_birth_year()                                     # repeat main function
            else:                                                    # otehrwise
                break                                                # go to the next step
        except ValueError:                                           # except if input = wrong type
            error_non_integer_input()                                # then throw this error function, loop repeats

def calculate_enrollment_year():
    """To calculate user's age and expected enrollment year"""

    global current_year, current_age, grown_up_age, enrollment_year

    current_age = current_year - input_birth_year
    enrollment_year = input_birth_year + grown_up_age


def throw_result():
    """To fill up a string with collected data."""

    global enrollment_year

    expired = (steps_colored[4], f'{colors[0]}{input_birth_year}{colors[7]}', current_age, f'{colors[4]}NO{colors[7]}', enrollment_year)
    success = (steps_colored[4], f'{colors[0]}{input_birth_year}{colors[7]}', current_age, f'{colors[4]}YES{colors[7]}', 'THIS YEAR')
    failure = (steps_colored[4], f'{colors[0]}{input_birth_year}{colors[7]}', current_age, f'{colors[4]}NO{colors[7]}', enrollment_year)

    result_text = \
    """
    {}
    ================================
    # 1. User's birth year:        # [ {} ]
    # 2. Current age:              # [ {} years old ]
    # 3. Allowed to enroll?:       # [ {} ]
    # 4. Enrollment year excepted: # [ {} ]
    ================================
    """

    if enrollment_year < current_year:
        print(result_text.format(*expired))
    elif enrollment_year == current_year:
        print(result_text.format(*success))
    else:
        print(result_text.format(*failure))

    input(f'\n{colors[0]}    Press ANY KEY to reset the algorithm...{colors[7]}\n')

while True:
    welcome('Army enrollment checker')
    start()
    if input_algorithm_start in algorithm_closure:
        print(closure)
        break
    instructions()
    get_birth_year()
    calculate_enrollment_year()
    throw_result()
