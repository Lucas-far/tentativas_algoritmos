

from methods_database import (
    get_input_integer, input_printer, instructions, welcome, step_painter, number_maker_by_difficulty, calculus_printer,
    operator_finder, math_maker, tell_if_this_basic_math_true, message_frame
)

from widgets import (
    click_arrow, colors, hit_enter, the_breaking_point, the_closure
)

# input values are set to the minimum value possible for their purpose
input_difficulty: int = 1
input_user_guess: int = - 100_000_000
user_points: int = 0

while True:

    # guide user's steps -----------------------------------------------------------------------------------------------
    steps = step_painter(
        '',
        '1 - The instructions',
        '2 - Pick difficulty',
        '3 - Tell your guess',
        '4 - Current result',
        '5 - Definite result',
        prefix=3,
        prefix2=7
    )

    # greetings --------------------------------------------------------------------------------------------------------
    print(greetings := welcome('Math game'))

    # procedures of the algorithm --------------------------------------------------------------------------------------
    print(steps[1])
    print(the_instructions := instructions(
        content="""
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

    # content controller -----------------------------------------------------------------------------------------------
    input_printer()

    # integer input to collect math difficulty -------------------------------------------------------------------------
    print(steps[2])
    input_difficulty = get_input_integer(
        the_input=input_difficulty,
        input_text=f"""
        ======= QUESTION: {colors[0]}What difficulty do you want?{colors[7]} =======
        Type one of the integers below, to pick the level of the calculus

            1 = easy
            2 = average
            3 = challenge
            4 = insanity

        A - {click_arrow}
        B - {hit_enter}
        -------> """,
        initial_target=1,
        ending_target=4
    )
    """print("input_difficulty =", input_difficulty)"""  # remove quotes to see results

    # make two random values and one operator for the calculus ---------------------------------------------------------
    the_first_value, the_second_value = number_maker_by_difficulty(
        the_difficulty=input_difficulty,
        alternative=False,
        alternative2=False
    )
    """print("the_first_value =", the_first_value)"""    # remove quotes to see results
    """print("the_second_value =", the_second_value)"""  # remove quotes to see results

    # to place the calculus as a question into a string ----------------------------------------------------------------
    calculus_message = calculus_printer(
        value_one=the_first_value, value_two=the_second_value, alternative_operator=False
    )
    """print("calculus_message =", calculus_message)"""  # remove quotes to see results

    # integer input to collect user's calculus guess -------------------------------------------------------------------
    print(steps[3])
    input_user_guess = get_input_integer(
        the_input=input_user_guess,
        input_text=f"""
        ======= QUESTION: {colors[0]}{calculus_message}{colors[7]} =======
        A - {click_arrow}
        B - Type how much is your guess (maximum is 100 million)
        B - {hit_enter}
        -------> """,
        initial_target=- 100_000_000,
        ending_target=100_000_000
    )
    """print("input_user_guess =", input_user_guess)"""  # remove quotes to see results

    # get the random operator previously generated for further use -----------------------------------------------------
    the_operator = operator_finder(text=calculus_message, alternative_operator=False)
    """print("the_operator =", the_operator)"""  # remove quotes to see results

    # as the operator is detected, values can be calculated and result becomes available -------------------------------
    math_result = math_maker(value_one=the_first_value, value_two=the_second_value, the_operator=the_operator)
    """print("math_result =", math_result)"""  # remove quotes to see results


    # the_truth = math_result == input_user_guess ----------------------------------------------------------------------
    the_truth = tell_if_this_basic_math_true(
        value_one=the_first_value, value_two=the_second_value, the_operator=the_operator, the_result=input_user_guess
    )
    """print("the_truth =", the_truth)"""  # remove quotes to see results

    # inputs have to be reset to their inittial values -----------------------------------------------------------------
    input_difficulty: int = 1
    input_user_guess: int = - 100_000_000

    # count user's points as the algotithm resets, or breaks it as user provides a wrong guess--------------------------
    if not the_truth:
        print(steps[5])
        print(message_frame(f'Resposta incorreta. Você terminou com {user_points} ponto(s).'))
        print(the_closure)
        break
    else:
        user_points += 1
        print(steps[4])
        print(message_frame(f'Você está com {user_points} ponto(s).'))

    # any key will continue the game, except key 'n', which breaks it --------------------------------------------------
    go_on = input_printer('\n========== DÚVIDA ==========\nVocê deseja continuar jogando? se não, digite "n" e aperte ENTER\n -> ')
    if go_on in the_breaking_point:
        print(steps[5])
        print(message_frame(f'Você terminou com {user_points} ponto(s).'))
        print(the_closure)
        break
