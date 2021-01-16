

# from name_shapping import *
# get_name()

from resources import *
from error_handling import string_incompatible_data, mistake_at_string

input_name = None
input_name_shaped = None
index = 0
wrong_character_seeker = []


def get_name():
    """To throw input to ask and collect person's name"""

    global input_name, index

    label = f'\n{colors[2]}Provide input: name{colors[7]}\n'

    input_text = \
    f"""
    {label}
    {colors[0]}What is your name?{colors[7]}
    1. {click_arrow}
    2. Type your name
    3. {press_enter_key}
    -> """

    # To control repetition of the algorithm
    while True:
        input_name = input(input_text)
        while index < len(input_name):
            wrong_character_seeker.append(input_name[index] in string_incompatible_data)
            index += 1

        # Group of conditions to check improper data
        if True in wrong_character_seeker \
        or input_name == '' \
        or input_name == ' ' \
        or len(input_name) < 2:

            print(mistake_at_string)
            index = 0                       # to set back to zero in order to check next new input
            wrong_character_seeker.clear()  # to clean list in order to check next new input
            get_name()                      # to repeat function in case of improper data

        else:
            # name_shaper(input_name)         # to shape name in case all conditions above were False
            # print(input_name_shaped)        # to print name fully shaped
            index = 0
            wrong_character_seeker.clear()
            break

        break                               # To cease the matrix loop


def name_shaper(data_name):
    """To turn a name with grammatical issues into a grammarly appropriated name"""

    global input_name_shaped

    name_discard_useless_spacing = data_name.split()

    name_proper_spacing = ' '.join(name_discard_useless_spacing)

    name_proper_grammar = f'{colors[3]}{name_proper_spacing.title()}{colors[7]}'

    input_name_shaped = name_proper_grammar
