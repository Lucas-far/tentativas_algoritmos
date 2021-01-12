

from methods_database import (
    colors, calculate_lifetime, customize_birthday, customize_birthday_str,  find_sign, get_input_integer, instructions,
    should_algorithm_run, welcome
)

from widgets import (
    click_arrow, hit_enter, the_breaking_point, the_closure
)

steps: tuple = ('',
                '1 - Should algorithm run?',
                '2 - Display of instructions',
                '3 - Provide input: birth day',
                '4 - Provide input: birth month',
                '5 - Provide input: birth year',
                '6 - Display of result')

steps: tuple = tuple([f'\n{colors[2]}{step}{colors[7]}\n' for step in steps])

input_exec: str = ''
input_birth_day: int = 1
input_birth_month: int = 1
input_birth_year: int = 1

def start():
    """"""
    global input_exec
    print(steps[1])
    input_exec = input(should_algorithm_run())

while True:

    welcome('Sign Identifier')
    start()

    if input_exec in the_breaking_point:
        print(the_closure)
        break

    instructions(
        the_content=f"""
        {steps[2]}
        ========== INSTRUCTIONS ==========
        1 - Provide your {colors[1]}birth day{colors[7]}
        2 - Provide your {colors[1]}birth month{colors[7]}
        3 - Provide your {colors[1]}birth year{colors[7]}
        4 - The algorithm will return user's sign and lifetime existence
        """
    )

    input_birth_day = get_input_integer(
        the_input=input_birth_day,
        input_text=f"""
        {steps[3]}
        ======= QUESTION: {colors[0]}In what day have you been born?{colors[7]} =======
        1 - {click_arrow}
        2 - Type the day you have been born (from 1 to 31)
        3 - {hit_enter}
        -------> """,
        the_initial_integer=1,
        the_last_integer=31
    )

    input_birth_month = get_input_integer(
        the_input=input_birth_month,
        input_text=f"""
        {steps[4]}
        ======= QUESTION: {colors[0]}In what month have been born?{colors[7]} =======
        1 - {click_arrow}
        2 - Type the month you have been born (from 1 to 12)
        3 - {hit_enter}
        -------> """,
        the_initial_integer=1,
        the_last_integer=12
    )

    input_birth_year = get_input_integer(
        the_input=input_birth_year,
        input_text=f"""
        {steps[5]}
        ======= QUESTION: {colors[0]}In what year have you been born?{colors[7]} =======
        1 - {click_arrow}
        2. Type the year you have been born (from year 1 to 9999)
        3 - {hit_enter}
        -------> """,
        the_initial_integer=1,
        the_last_integer=9_999
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

    the_report = find_sign(
        birthday=user_birthday_str,
        existence=user_lifetime,
        day=input_birth_day,
        month=input_birth_month
    )

    print(the_report)

    input_birth_day: int = 1
    input_birth_month: int = 1
    input_birth_year: int = 1
