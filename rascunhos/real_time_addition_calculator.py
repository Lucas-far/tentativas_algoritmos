

"""
requirements = (
    ('resources', 'module which holds complementary functions and variables with instructions')
)
"""

from resources import *

input_algorithm_procedure: str = ''  # start()

input_number: float = 0.0            # throw_result()
numbers_storage: list = []           # throw_result()


steps: tuple = ('',
                '1 - Should algorithm run?',
                '2 - Display of instructions',
                '3 - Provide: number to calculate (1 by 1)',
                '4 - Display of result'
                )

steps_painted: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n' for each_data in steps])


def start():
    """To ask if algorithm must or not run. If user provides string 'end', the algorithm ceases."""

    global input_algorithm_procedure

    print(steps_painted[1])

    input_algorithm_procedure = input(doubt_run_algorithm)


def instructions():
    """To inform procedures of the algorithm"""

    instruction_text = \
    f"""
    {steps_painted[2]}
    1. It will be asked an integer or non-integer value, so provide one (either negative or positive)
    2. If current input is a negative number, the list will be subtracted
    3. If current input is a positive number, the list will be summed
    4. After each new number added, it will be thrown the current total and the numbers added so far
    5. Type number {colors[3]}0{colors[7]} in order to cease the math"""

    print(instruction_text)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...


def throw_result():
    """To treat improper data while a proper integer or floating number is not being provided."""

    global input_number, numbers_storage

    partial_total: str = \
    """
    {}
    Current numbers: {}
    Partial Total: {}{:.2f}{}
    """

    total: str = \
    """
    {}
    ========== RESULT ==========
    The sum of all number is: {}{:.2f}{}
    """

    input_text: str = \
    f"""
    {steps_painted[3]}
    {colors[0]}What number do you want to add?{colors[7]} 
    1. {click_arrow}
    2. Type a number (integer or floating) (positive or negative)
    3. Or type {colors[3]}0{colors[7]} to cease the sum
    3. {press_enter_key}
    -> """

    while True:

        try:

            input_number = float(input(input_text))

            if input_number != 0:

                numbers_storage.append(input_number)

                print(partial_total.format(
                    steps_painted[4], numbers_storage, colors[4], sum(numbers_storage), colors[7]))

            else:

                print(total.format(
                    steps_painted[4], colors[4], sum(numbers_storage), colors[7]))

                numbers_storage = []

                input(f'\n{colors[0]}Press ANY KEY to reset the algorithm...{colors[7]}\n')

                break

        except ValueError:                 # if input = wrong type
            error_non_numerical_input()    # throw this error function, loop repeats

while True:
    welcome('Real time addition calculator')
    start()
    if input_algorithm_procedure in algorithm_cease:  # if user provides 'end' = end of the algorithm
        print(closure)
        break
    instructions()
    throw_result()
