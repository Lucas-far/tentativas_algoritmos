

from methods_database import (
    get_input_integer, input_printer, instructions, should_algorithm_run, welcome, step_painter
)

from method_drafts import (
    number_maker_by_difficulty, calculus_printer, operator_finder, math_maker, tell_if_this_basic_math_true,
)

from widgets import (
    click_arrow, colors, hit_enter, the_breaking_point, the_closure
)

# single use input to determine the start of the algorithm
input_exec: str = ''

# input values are set to the minimum value possible for their purpose
input_difficulty: int = 1
input_user_guess: int = - 100_000_000
user_points: int = 0

def start():
    """"""
    global input_exec
    print(steps[1])
    input_exec = input(should_algorithm_run())

while True:

    # colorize title steps
    steps = step_painter(
            '',
            '1 - Should algorithm run?',
            '2 - Display of instructions',
            '3 - Pick difficulty',
            '4 - Tell your guess',
            '5 - Current result',
            prefix=3,
            prefix2=7
        )

    # inittial message of the algorithm
    print(greetings := welcome('Math tester'))

    # algorithm starts here
    start()

    # algorithm progress is defined here
    if input_exec in the_breaking_point:
        print(the_closure)
        break

    # data to understand the algorithm
    print(the_instructions := instructions(
        content=f"""
        {steps[2]}
        ========== INSTRUCTIONS ==========
        1  - The goal is to test your calcuting skills
        2  - It will be asked the difficulty of the calculus (1 to 4) easiest to hardest
        3  - Use the input to provide the difficulty
        4  - One math procedure will be created upon your choice
        5  - This calculus will be shown to you 
        6  - Use the input to provide an answer
        7  - It will be checked if your answer is correct
        8  - If yes, you will have points added 1 by 1
        9  - If not, you will be kicked out of the game
        """
    ))

    # to create a content blockage
    input_printer()

    # first input is collected here
    input_difficulty = get_input_integer(
        the_input=input_difficulty,
        input_text=f"""
        {steps[3]}
        ======= QUESTION: {colors[0]}What difficulty do you want?{colors[7]} =======

        Type one of the integers below, to pick the level of the calculus

            1 = easy
            2 = average
            3 = challenge
            4 = insanity

        A - {click_arrow}
        B - {hit_enter}
        -------> """,
        the_initial_integer=1,
        the_last_integer=4
    )

    # the method returns two values, they become values of both variables
    the_first_value, the_second_value = number_maker_by_difficulty(the_difficulty=input_difficulty)

    # to create a fstring with the numbers, to ask user about an answer
    calculus_message = calculus_printer(value_one=the_first_value, value_two=the_second_value)

    # second input is collected here to get what user thinks to be the result
    input_user_guess = get_input_integer(
        the_input=input_user_guess,
        input_text=f"""
        {steps[4]}
        ======= QUESTION: {colors[0]}{calculus_message}{colors[7]} =======

        A - {click_arrow}
        B - Type how much is your guess (maximum is 100 million)
        B - {hit_enter}
        -------> """,
        the_initial_integer=- 100_000_000,
        the_last_integer=100_000_000
    )

    # if there is a string operator through a string, it will be found, taken and used for the next step
    the_operator = operator_finder(text=calculus_message)

    # when the operator is detected, the previous values are calculated
    math_result = math_maker(value_one=the_first_value, value_two=the_second_value, the_operator=the_operator)

    # if the math of the algorithm == user's guess, this will return True
    the_truth = tell_if_this_basic_math_true(
        value_one=the_first_value, value_two=the_second_value, the_operator=the_operator, the_result=input_user_guess
    )

    # inputs have to be reset to their inittial values
    input_difficulty: int = 1
    input_user_guess: int = - 100_000_000

    # this will count user's points as the algotirhm resets, breaking it if user provides a wrong guess
    if not the_truth:
        the_breakpoint: str = f'Resposta incorreta. Você terminou com {user_points} ponto(s).'
        print(the_breakpoint)
        break
    else:
        user_points += 1
        message_success: str = f'Você está com {user_points} ponto(s).'
        print(steps[5])
        print(message_success)
