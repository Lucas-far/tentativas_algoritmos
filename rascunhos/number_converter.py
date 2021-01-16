

from resources import *

input_algorithm_start: str = ''

input_number: int = 0

input_conversion_type: int = 0

counter: int = 0

repetition_boundary: int = 5

index: int = 0

steps: tuple = ('', '1 - Should algorithm run?', '2 - Display of Instructions', '3 - Provide input: number',
                '4 - Provide input: conversion type', '5 - Display of result')

steps_painted: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n' for each_data in steps])


def start():
    """To ask if algorithm must or not run. If user provides (str) 'end': break. Else: continue."""

    global input_algorithm_start

    print(steps_painted[1])

    input_algorithm_start = input(doubt_run_algorithm)


def instructions():
    """To inform procedures of the algorithm."""

    instructions_text: str = \
    f"""
    {steps_painted[2]}
    1. Provide input: number
    2. Provide input: type of conversion
    3. It will be returned the proper conversion based on the provided data"""

    print(instructions_text)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...


def get_number():
    """To treat improper data while a proper integer number is not being provided."""

    global input_number

    input_text = \
    f"""
    {steps_painted[3]}
    {colors[0]}What is the number to be converted?{colors[7]}
    1. {click_arrow}
    2. Type any integer number, negative or positive
    3. {press_enter_key}
    -> """

    while True:
        try:
            input_number = int(input(input_text))
            break
        except ValueError:
            print('\n')
            print(announcement)
            print('The input only allows numbers: integer + - or floating + -')


def get_conversion_type():
    """To treat improper data while a proper integer number is not being provided."""

    global input_conversion_type

    input_text = \
    f"""
    {steps_painted[4]}
    {colors[0]}What kind of conversion do you want?{colors[7]}
    1. {click_arrow}
        Type {colors[1]}0 for binary{colors[7]} 
        Type {colors[2]}1 for complex{colors[7]} 
        Type {colors[3]}2 for floating{colors[7]} 
        Type {colors[4]}3 for hexadecimal{colors[7]} 
        Type {colors[5]}4 for integer{colors[7]} 
        Type {colors[6]}5 for octal{colors[7]} 
    2. {press_enter_key}
    -> """

    while True:
        try:
            input_conversion_type = int(input(input_text))
            while input_conversion_type < 0 or input_conversion_type > 5:  # while input = improper number
                error_input_integer_out_of_range(0, 5)                     # throw this error function
                get_conversion_type()                                      # repeat main function
            else:                                                          # otherwise
                break                                                      # go to the next step
        except ValueError:                                                 # except if input = wrong type
            error_input_integer_not_used(0, 5)                             # then thro this erro function, loop repeats


def throw_result():
    """To fill a string will collected data."""

    global counter, index, repetition_boundary

    conversion_categories: tuple = ('Binary', 'Complex', 'Floating', 'Hexadecimal', 'Integer', 'Octal')

    conversion_categories_painted: tuple = tuple([f'{colors[0]}{each_data}{colors[7]}' for each_data in conversion_categories])

    conversion_procedures: tuple = (bin(input_number)[2:], complex(input_number), float(input_number),
                                    hex(input_number), int(input_number), oct(input_number)[2:])

    result: str = \
    """
    {}
    =======================
    # Provided number     # {}
    # Type of conversion  # {}
    # Conversion result   # {}
    =======================
    """

    while counter <= repetition_boundary:  # number of indexes of possible conversions = 5
        if input_conversion_type == counter:
            print(result.format(steps_painted[5], input_number, conversion_categories_painted[index], conversion_procedures[index]))
            break
        else:
            counter += 1
            index += 1
    counter = 0
    index = 0

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...

while True:
    welcome('Number converter')
    start()
    if input_algorithm_start in algorithm_cease:
        print(closure)
        break
    instructions()
    get_number()
    get_conversion_type()
    throw_result()
