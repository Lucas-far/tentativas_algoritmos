

# todo -> Edição do algoritmo (atualmente nas variáveis)

"""
Requirements
------------

1. resources (type="module") to import variables and functions
"""

from resources import *

# Inputs in order of occurrence
input_algorithm_procedure: str = ''
input_integer_number: int = 0

# Variables targeted to calculus
ones: int = 0
tens: int = 0
hundreds: int = 0
thousands: int = 0
ten_thousands: int = 0
hundred_thousands: int = 0
millions: int = 0

conditions: list = []                # build_conditions()
target_index: int = 0                # build_conditions()
possibilities: tuple = ()            # build_conditions()
absent: str = 'not found'            # build_conditions()
index_outset: tuple = ()      # build_conditions()
index_closure: tuple = ()       # build_conditions()
perform_slice: tuple = ()                 # build_conditions()

result_text: str = ''                # throw_result()

steps: tuple = ('', '1. Should algorithm run?', '2. Display of instructions', '3. Provide input: integer number',
                '4. Display of result')

steps_colored: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n'for each_data in steps])


def start():
    """To ask if algorithm must or not run. If user provides (str) 'end': break. Else: continues."""

    global input_algorithm_procedure

    print(steps_colored[1])

    input_algorithm_procedure = input(doubt_run_algorithm)


def instructions():
    """To inform procedures of the algorithm."""

    instruction_text: str = \
    f"""
    {steps_colored[2]}
    1. Provide an integer number with digits between 1 to 7
    2. Each number will be placed at its proper decimal field"""

    print(instruction_text)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...


def get_integer_number():
    """To treat improper data while a proper integer number is not being provided."""

    global input_integer_number

    input_text: str = \
    f"""
    {steps_colored[3]}
    {colors[0]}What is the integer to be split?{colors[7]} 
    1. {click_arrow}
    2. Type an integer number between 1 to 7 digits
    3. {press_enter_key}
    -> """

    error_input_out_of_range: str = \
    f"""
    {announcement}
    1. The provided input is out of the allowed range: {colors[0]}0 to any number{colors[7]}
    """

    error_input_wrong_type = \
    f"""
    {announcement}
    The provided input must be a positive integer between 1 to 7 digits length
    """

    while True:
        try:
            input_integer_number = int(input(input_text))
            while input_integer_number <= 0 or input_integer_number > 9_999_999:  # while input = improper number
                print(error_input_out_of_range)                                   # print this error
                get_integer_number()                                              # repeat main function
            else:                                                                 # otherwise
                break                                                             # go to the next step
        except ValueError:                                                        # except if input = wrong type
            print(error_input_wrong_type)                                         # then print this error, loop repeats


def organize_digits_placement(integer: int = 0):
    """To get each digit of a value placed into its proper position"""

    global ones, tens, hundreds, thousands, ten_thousands, hundred_thousands, millions

    # ========== ASSUMPTION ========== input_integer_number = 1234567

    millions = str(integer // 1_000_000 % 10)         # millions          = '1'
    hundred_thousands = str(integer // 100_000 % 10)  # hundred thousands = '2'
    ten_thousands = str(integer // 10_000 % 10)       # ten thousands     = '3'
    thousands = str(integer // 1000 % 10)             # thousands         = '4'
    hundreds = str(integer // 100 % 10)               # hundreds          = '5'
    tens = str(integer // 10 % 10)                    # tens              = '6'
    ones = str(integer // 1 % 10)                     # ones              = '7'


def build_conditions():
    """To place possible conditions into a list and get the one which returns True"""

    global conditions, target_index, possibilities, index_outset, index_closure, perform_slice

    conditions = [
        [True if input_integer_number < 10 else None],
        [True if 10 <= input_integer_number < 100 else None],
        [True if 100 <= input_integer_number < 1_000 else None],
        [True if 1_000 <= input_integer_number < 10_000 else None],
        [True if 10_000 <= input_integer_number < 100_000 else None],
        [True if 100_000 <= input_integer_number < 1_000_000 else None],
        [True if 1_000_000 <= input_integer_number < 10_000_000 else None]
    ]

    # ========== TUTORIAL ========== -> If [True] in conditions[5]: target_index = 5
    target_index = conditions.index([True])

    possibilities = (absent, absent, absent, absent, absent, absent, ones,
                     absent, absent, absent, absent, absent, tens, ones,
                     absent, absent, absent, absent, hundreds, tens, ones,
                     absent, absent, absent, thousands, hundreds, tens, ones,
                     absent, absent, ten_thousands, thousands, hundreds, tens, ones,
                     absent, hundred_thousands, ten_thousands, thousands, hundreds, tens, ones,
                     millions, hundred_thousands, ten_thousands, thousands, hundreds, tens, ones)


    # index_outset gets linked with index_closure
    # index_outset[0]:index_closure[0] = 1st condition
    # index_outset[1]:index_closure[1] = 2nd condition
    # so on so forth...
    index_outset = (0, 7, 14, 21, 28, 35, 42)
    index_closure = (7, 14, 21, 28, 35, 42, 49)

    perform_slice = possibilities[index_outset[target_index]:index_closure[target_index]]

    # ========== TUTORIAL ==========
    # Assumption: [True] in conditions[0]

    # If [True] in conditions[0], then: target_index = 0
    # perform_slice = possibilities[index_outset[target_index]:index_closure[target_index]]
    # perform_slice = possibilities[index_outset[0]:index_closure[0]]
    # perform_slice = possibilities[0:7]
    # *perform_slice = absent, absent, absent, absent, absent, absent, ones


def throw_result():
    """To print result coming from conditions and possibilities."""

    global result_text

    result_text = \
    """
    {}
    Target number: [ {} ]

    Millions         = [ {} ]
    Hundred thousand = [ {} ]
    Ten thousand     = [ {} ]
    Thousand         = [ {} ]
    Hundreds         = [ {} ]
    Tens             = [ {} ]
    Ones             = [ {} ]
    """

    print(result_text.format(steps_colored[4], input_integer_number, *perform_slice))

    input(f'\n{colors[0]}    Press ANY KEY to reset the algorithm...{colors[7]}\n')

while True:
    welcome('Decimal Place Splitter')
    start()
    if input_algorithm_procedure in algorithm_cease:  # if user provides 'end' = end of the algorithm
        print(closure)
        break
    instructions()
    get_integer_number()
    organize_digits_placement(input_integer_number)
    build_conditions()
    throw_result()
