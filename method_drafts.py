

from random import choice, randint

def number_maker_by_difficulty(the_difficulty: int = 1):
    """"""
    # calculus = '========== Quanto é {} {} {}? =========='

    if the_difficulty == 1:
        easy = randint(1, 9)
        easy2 = randint(1, 9)
        return easy, easy2

    elif the_difficulty == 2:
        average = randint(9, 15)
        average2 = randint(9, 15)
        return average, average2

    elif the_difficulty == 3:
        challenging = randint(15, 50)
        challenging2 = randint(15, 50)
        return challenging, challenging2

    else:
        insane = randint(100, 10_000)
        insane2 = randint(100, 10_000)
        return insane, insane2

    # operators = ['+', '-', 'x']
    # calculus = '========== Quanto é {} {} {}? =========='

    # if the_difficulty == 1:
    #     easy = randint(1, 9)
    #     easy2 = randint(1, 9)
        # the_operator = choice(operators)
        # print(calculus.format(easy, the_operator, easy2))
        #
        # calculus_table_level_easy = ((easy + easy2), (easy - easy2), (easy * easy2))
        #
        # if the_operator == '+':
        #     return calculus_table_level_easy[0]
        # elif the_operator == '-':
        #     return calculus_table_level_easy[1]
        # else:
        #     return calculus_table_level_easy[2]

    # elif the_difficulty == 2:
    #     average = randint(9, 15)
    #     average2 = randint(9, 15)
        # the_operator = choice(operators)
        # print(calculus.format(average, the_operator, average2))
        #
        # calculus_table_level_average = ((average + average2), (average - average2), (average * average2))
        #
        # if the_operator == '+':
        #     return calculus_table_level_average[0]
        # elif the_operator == '-':
        #     return calculus_table_level_average[1]
        # else:
        #     return calculus_table_level_average[2]

    # elif the_difficulty == 3:
    #     challenging = randint(15, 50)
    #     challenging2 = randint(15, 50)
        # the_operator = choice(operators)
        # print(calculus.format(challenging, the_operator, challenging2))
        #
        # calculus_table_level_challenging = (
        #     (challenging + challenging2), (challenging - challenging2), (challenging * challenging2)
        # )
        #
        # if the_operator == '+':
        #     return calculus_table_level_challenging[0]
        # elif the_operator == '-':
        #     return calculus_table_level_challenging[1]
        # else:
        #     return calculus_table_level_challenging[2]

    # else:
    #     insane = randint(100, 10_000)
    #     insane2 = randint(100, 10_000)
        # the_operator = choice(operators)
        # print(calculus.format(insane, the_operator, insane2))
        #
        # calculus_table_level_insane = ((insane + insane2), (insane - insane2), (insane * insane2))
        #
        # if the_operator == '+':
        #     return calculus_table_level_insane[0]
        # elif the_operator == '-':
        #     return calculus_table_level_insane[1]
        # else:
        #     return calculus_table_level_insane[2]

def calculus_printer(value_one: int = 1, value_two: int = 1):
    """"""
    operators = ['+', '-', 'x']
    calculus = f'========== Quanto é {value_one} {choice(operators)} {value_two}? =========='
    return calculus

def operator_finder(text: str = ''):
    """"""
    operators = ['+', '-', 'x', '/']
    box = []

    for obj in operators:
        box.append(obj in text)
        if True in box:
            break
    operator_found = operators[box.index(True)]

    return operator_found

def math_maker(value_one: int = 1, value_two: int = 1, the_operator: str = ''):
    """"""
    calculus_table = ((value_one + value_two), (value_one - value_two), (value_one * value_two))

    if the_operator == '+':
        return calculus_table[0]
    elif the_operator == '-':
        return calculus_table[1]
    else:
        return calculus_table[2]

def tell_if_this_basic_math_true(value_one: int = 1, value_two: int = 1, the_operator: str = '', the_result: int = 0):
    """"""
    if the_operator == '+':
        return (value_one + value_two) == the_result
    elif the_operator == '-':
        return (value_one - value_two) == the_result
    elif the_operator == 'x':
        return (value_one * value_two) == the_result
    else:
        return None

def true_counter(the_comparison):
    """"""
    counter = 0

    if the_comparison:
        counter += 1
        return counter

    counter = 0
    return counter

if __name__ == '__main__':
    # var = calculus_generator_and_manager(the_difficulty=2)
    # print(var)
    print(operator_finder('Quanto é 20 * 7?x'))
    pass
