

from error_handling import mistake_at_string, string_incompatible_data
from resources import *
from statistics import mean

# Inputs in order of occurrence
input_algorithm_start: str = ''
input_name: str = ''
input_name_shaped: str = ''
input_grades: float = 0.0

# Variables for calculus and comparison
acceptable_mean = 7
grade_max = 10
grade_zero = 0
index = 0
student_mean: float = 0.0

# Variables for checkage and storage
wrong_character_seeker = []
grades_storage = []

# Variables to inform
steps: tuple = ('', '1 - Should algorithm run?', '2 - Display of instructions', '3 - Provide input: grade',
                '4 - Continue to add grades?', '5 - Display of result')

steps_painted: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n' for each_data in steps])


def start():
    """"""

    global input_algorithm_start

    print(steps_painted[1])

    input_algorithm_start = input(doubt_run_algorithm)


def get_name():
    """To get someone's string name containing the correct alphabetical characters"""

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

    while True:
        input_name = input(input_text)

        # Temporary loop to check if a wrong character has been found
        while index < len(input_name):
            wrong_character_seeker.append(input_name[index] in string_incompatible_data)
            index += 1

        # Group of conditions to check improper input
        if True in wrong_character_seeker \
        or input_name == '' \
        or input_name == ' ' \
        or len(input_name) < 2:

            print(mistake_at_string)
            index = 0                       # if improper data, reset it
            wrong_character_seeker.clear()  # if improper data, clean it
            get_name()                      # if improper data, repeat it

        else:                               # if proper data
            index = 0                       # reset it
            wrong_character_seeker.clear()  # clean it
        break                               # go to the next step


def name_shaper(data_name):
    """To treat input name with grammatical issues to an appropriate name"""

    global input_name_shaped

    name_discard_useless_spacing = data_name.split()

    name_proper_spacing = ' '.join(name_discard_useless_spacing)

    name_proper_grammar = f'{colors[3]}{name_proper_spacing.title()}{colors[7]}'

    input_name_shaped = name_proper_grammar


def instructions():
    """To print procedures of the algorithm."""

    instructions_text = \
    f"""
    {steps_painted[2]}
    1. Provide input: student's grades one by one
    2. When you are done, type the word 'no' to finish adding grades
    3. The student's mean will be calculated and a message will inform approval or failure"""

    print(instructions_text)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...


def get_all_grades():
    """To treat improper data while a proper integer/floating number is not being provided."""

    global input_grades

    input_text = \
    f"""
    {steps_painted[3]}
    {colors[0]}What is the student's grade?{colors[7]} 
    1. {click_arrow}
    2. Type the student's grade
    3. {press_enter_key}
    -> """

    while True:
        try:
            input_grades = float(input(input_text))
            grades_storage.append(input_grades)

            while input_grades < grade_zero or input_grades > grade_max:
                error_input_floating_out_of_range(0.0, 10.0)
                get_all_grades()
            else:
                break
        except ValueError:
            error_input_floating_not_used(0.0, 10.0)


def add_next_grade():
    """To ask if the procedure of adding grades must continue."""

    input_text2 = \
    f"""
    {steps_painted[4]}
    {colors[0]}Do you wish to add one next grade?{colors[7]} 
    1. {click_arrow}
    2. Type any key to continue adding grades
    3. Type {colors[1]}no{colors[7]} to throw the calculus of the mean
    4. {press_enter_key}
    -> """

    while True:
        question: str = input(input_text2)
        while question != "no":
            get_all_grades()
            break
        else:
            break


def throw_result():
    """To fill a string with user's ultimate data."""

    global student_mean

    student_mean = mean(grades_storage)

    approved: tuple = (steps_painted[5], input_name_shaped, grades_storage, student_mean, 'APPROVED')

    failed: tuple = (steps_painted[5], input_name_shaped, grades_storage, student_mean, 'FAILED')

    result = \
    """
    {}
    =====================
    # Student's name:   # {}
    # Student's grades: # {}
    # Student's mean    # {}
    # Student's status: # {}
    =====================
    """

    if student_mean >= acceptable_mean:
        print(result.format(*approved))
    else:
        print(result.format(*failed))

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...

while True:
    welcome('Grade mean checker')
    start()
    if input_algorithm_start in algorithm_cease:
        print(closure)
        break
    get_name()
    name_shaper(input_name)
    instructions()
    get_all_grades()
    add_next_grade()
    throw_result()
