

from random import choice

from resources import *

input_algorithm_start: str = ''

input_data_type_option: int = 0

input_characters_length: int = 0

other_characters: list = ["'", '"', '¨', 'º', 'ª', '`', '´']  # Unused characters for being too small

characters: list = []

letters: list = []

numbers: list = []

loop_counter: int = 0

your_code: list = []

steps: tuple = ('', '1 - Should algorithm run?', '2 - Display of instructions', '3 - Provide input: data type',
                '4 - Provide input: length', '5 - Display of result')

steps_painted: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n' for each_data in steps])


def start():
    """To ask if algorithm must or not run. If user provides string 'end', the algorithm ceases."""

    global input_algorithm_start

    print(steps_painted[1])

    input_algorithm_start = input(doubt_run_algorithm)

def instructions():
    """To print procedures of the algorithm."""

    instructions_text: str = \
    f"""
    {steps_painted[2]}
    1. It will be asked options of data to be generated, therefore, pick one
    2. It will be asked how many characters to be generated, therefore, type how many
    3. It will be generated random characters based on the chosen option"""

    print(instructions_text)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...

def get_data_type():
    """To treat improper data while a proper integer number is not being provided."""

    global input_data_type_option

    input_text: str = \
    f"""
    {steps_painted[3]}
    {colors[0]}What option of data type do you want to generate?{colors[7]}
    1. {click_arrow}
    2. Provide a number corresponding to the option of your desire
    3. {press_enter_key}\n
    ========== OPTIONS ==========
    Type 1 to generate exclusively: characters
    Type 2 to generate exclusively: letters
    Type 3 to generate exclusively: numbers
    Type 4 to generate exclusively: characters with letters
    Type 5 to generate exclusively: letters with numbers
    Type 6 to generate exclusively: numbers with characters       
    -> """

    while True:
        try:
            input_data_type_option = int(input(input_text))
            while input_data_type_option < 1 or input_data_type_option > 6:  # while input = improper number
                error_input_integer_out_of_range(1, 6)                       # throw this error function
                get_data_type()                                              # repeat main function
            else:                                                            # otherwise
                break                                                        # go to the next step
        except ValueError:                                                   # except if input = wrong type
            error_input_integer_not_used(1, 6)                               # then throw this error function, loop repeats

def get_characters_length():
    """To treat improper data while a proper integer number is not being provided."""

    global input_characters_length

    input_text: str = \
    f"""
    {steps_painted[4]}
    {colors[0]}How many characters must your code have?{colors[7]}
    1. {click_arrow}
    2. Type an integer corresponding to the amount of characters
    3. {press_enter_key}
    -> """

    while True:
        try:
            input_characters_length = int(input(input_text))
            while input_characters_length <= 0:                  # while input = negative number
                error_input_integer_out_of_range(1, 'infinity')  # throw this error function
                get_characters_length()                          # repeat main function
            else:                                                # otherwise
                break                                            # go to the next steps
        except ValueError:                                       # except if input = wrong type
            error_input_integer_not_used(1, 'infinity')          # then throw this error function, loop repeats

def throw_result():
    """To fill up a list with collected data and unpack them in a loop for."""

    global characters, letters, loop_counter, numbers, your_code

    characters = [each_data for each_data in '[]{}!?/\\|()=+-_¬~*<>^@#$%&£¢:;,.']

    letters = [each_data for each_data in 'abcdefghijklmnopqrstuvwxyz']

    numbers = [str(each_data) for each_data in range(0, 10)]

    while loop_counter < input_characters_length:
        if input_data_type_option == 1:
            your_code.extend(choice(characters))
            loop_counter += 1
        elif input_data_type_option == 2:
            your_code.extend(choice(letters))
            loop_counter += 1
        elif input_data_type_option == 3:
            your_code.extend(choice(numbers))
            loop_counter += 1
        elif input_data_type_option == 4:
            your_code.extend(choice(characters))
            your_code.extend(choice(letters))
            loop_counter += 2
        elif input_data_type_option == 5:
            your_code.extend(choice(letters))
            your_code.extend(choice(numbers))
            loop_counter += 2
        elif input_data_type_option == 6:
            your_code.extend(choice(numbers))
            your_code.extend(choice(characters))
            loop_counter += 2

    your_code_str = ''.join(your_code)  # to convert the entire list of generated data into a single string

    result: str = \
    f"""
    {steps_painted[5]}
    {colors[4]}========== Generated code =========={colors[7]}
    {colors[0]}{your_code_str}{colors[7]}
    """

    print(result)

    loop_counter = 0

    your_code.clear()

    input(f'\n{colors[0]}Press ANY KEY to reset the algorithm...{colors[7]}\n')

    # if input_data_type_option == 1:
    #     while loop_counter < input_characters_length:
    #         your_code.extend(choice(characters))
    #         loop_counter += 1
    #
    # elif input_data_type_option == 2:
    #     while loop_counter < input_characters_length:
    #         your_code.extend(choice(letters))
    #         loop_counter += 1
    #
    # elif input_data_type_option == 3:
    #     while loop_counter < input_characters_length:
    #         your_code.extend(choice(numbers))
    #         loop_counter += 1
    #
    # elif input_data_type_option == 4:
    #     while loop_counter < input_characters_length:
    #         your_code.extend(choice(characters))
    #         your_code.extend(choice(letters))
    #         loop_counter += 2
    #
    # elif input_data_type_option == 5:
    #     while loop_counter < input_characters_length:
    #         your_code.extend(choice(letters))
    #         your_code.extend(choice(numbers))
    #         loop_counter += 2
    #
    # elif input_data_type_option == 6:
    #     while loop_counter < input_characters_length:
    #         your_code.extend(choice(numbers))
    #         your_code.extend(choice(characters))
    #         loop_counter += 2

    # print('\nYour code is:\n')
    # for each_data in your_code:
    #     print(f'{colors[0]}{each_data}{colors[7]}', end='')
    # loop_counter = 0
    # your_code.clear()

while True:
    welcome('Random characters generator')
    start()
    if input_algorithm_start in algorithm_cease:
        print(closure)
        break
    instructions()
    get_data_type()
    get_characters_length()
    throw_result()
