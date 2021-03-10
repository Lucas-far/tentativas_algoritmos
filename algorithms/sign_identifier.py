

from utils.methods_database import (
    calculate_lifetime, customize_birthday, customize_birthday_str,  find_sign, get_input_integer,
    instructions, should_algorithm_run, welcome, step_painter
)

from utils.strings_sign_identifier import *

from utils.widgets import (
    the_breaking_point, the_closure, to_proceed
)

input_exec: str = ''
input_birth_day: int = 1
input_birth_month: int = 1
input_birth_year: int = 1

steps = step_painter(
        '', '1 - Should algorithm run?', '2 - Display of instructions', '3 - Provide input: birth day',
        '4 - Provide input: birth month', '5 - Provide input: birth year', prefix=3, prefix2=7)

def start():
    """"""
    global input_exec
    print(steps[1])
    input_exec = input(should_algorithm_run())

while True:

    print(greetings := welcome('Sign Identifier'))
    start()

    if input_exec in the_breaking_point:
        print(the_closure)
        break

    print(the_instructions := instructions(
        content=f"{steps[2]}{instructions_text}"
    ))

    input(to_proceed)

    input_birth_day = get_input_integer(
        the_input=input_birth_day,
        input_text=f"{steps[3]}{input_text_which_day}",
        initial_target=1,
        ending_target=31
    )

    input_birth_month = get_input_integer(
        the_input=input_birth_month,
        input_text=f"{steps[4]}{input_text_which_month}",
        initial_target=1,
        ending_target=12
    )

    input_birth_year = get_input_integer(
        the_input=input_birth_year,
        input_text=f"{steps[5]}{input_text_which_year}",
        initial_target=1,
        ending_target=9_999
    )

    user_birthday = customize_birthday(
        year=input_birth_year,
        month=input_birth_month,
        day=input_birth_day
    )

    user_birthday_str = customize_birthday_str(
        year=input_birth_year,
        month=input_birth_month,
        day=input_birth_day
    )

    user_lifetime = calculate_lifetime(
        year=input_birth_year,
        month=input_birth_month,
        day=input_birth_day
    )

    print(the_report := find_sign(
        birthday=user_birthday_str,
        existence=user_lifetime,
        day=input_birth_day,
        month=input_birth_month
    ))

    input_birth_day: int = 1
    input_birth_month: int = 1
    input_birth_year: int = 1
