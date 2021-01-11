

""""""
colors: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m')

def calculate_lifetime(birthday, the_result):
    """
    To calculate user's lifetime.
    """

    from datetime import datetime

    today = datetime.today()
    the_existence_calculus = today - birthday
    the_result = f'About {str(the_existence_calculus).split()[0]} days'

    "Example"  # the_existence_calculus = 2020/07/08 - 1992/7/16 = 10219 days, 23:33:12.115426
    "Example"  # result = About 10219 days

    return the_result

def customize_birthday(the_birthday, the_birthday_srt: str = '', year: int = 1, month: int = 1, day: int = 1):
    """
    To build a datetime variable from a birthday.
    """
    from datetime import datetime

    the_birthday = datetime(year=year, month=month, day=day)
    the_birthday_srt = f'{year}/{month}/{day}'

    return the_birthday, the_birthday_srt

def find_sign(birthday, existence, existing_signs=12, day=1, month=1):
    """To custom conditions for each sign and print the result of the only possibility."""

    "Detail"   # The four variables below are arranged in the following sign order
    "Signs"    # [0] Capricorn [1] Aquarius [2] Pisces [3] Aries [4] Taurus [5] Gemini
    "Signs"    # [6] Cancer [7] Leo [8] Virgo [9] Libra [10] Scorpio [11] Sagittarius

    "Example"  # Capricorn = each_sign_first_month_days[0] and each_sign_first_month[0]
    "Example"  # Capricorn = each_sign_second_month_days[0] and each_sign_second_month[0]
    "Detail"   # Other signs follow the same pattern, only changing the indexes

    each_sign_first_month_days = (
        range(22, 32), range(21, 32), range(19, 32), range(21, 32), range(21, 32), range(21, 32),
        range(21, 32), range(23, 32), range(23, 32), range(23, 32), range(23, 32), range(22, 32)
    )

    each_sign_second_month_days = (
        range(1, 21), range(1, 19), range(1, 21), range(1, 21), range(1, 21), range(1, 21),
        range(1, 23), range(1, 23), range(1, 23), range(1, 23), range(1, 22), range(1, 22)
    )

    each_sign_first_month = (12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    each_sign_second_month = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

    signs: tuple = (
        'Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini',
        'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Saggitarius')

    the_result = \
        """
        ========== REPORT ==========
        Your birth: {}
        Your sign: {}
        Your days alive: {}
        """

    counter = 0
    while counter < existing_signs:

        if day in each_sign_first_month_days[counter] and month == each_sign_first_month[counter] \
         or day in each_sign_second_month_days[counter] and month == each_sign_second_month[counter]:

            return the_result.format(birthday, signs[counter], existence)

        else:
            counter += 1
    counter = 0

def get_input_integer(the_input, input_text, the_initial_integer, the_last_integer):
    """
    To treat improper data while a proper integer number is not being provided.
    """

    integer_out_of_range = f"""
        \033[1:31m========== ERROR ==========\033[m
        The provided input is not in the suitable range: {the_initial_integer} to {the_last_integer}"""

    integer_unused = f"""
        \033[1:31m========== ERROR ==========\033[m
        The provided input must be an integer number: {the_initial_integer} to {the_last_integer}"""

    while the_input <= the_initial_integer or the_input > the_last_integer:
        try:
            the_input = int(input(input_text))
            if the_input in range(the_initial_integer, the_last_integer + 1):
                break
            else:
                print(integer_out_of_range)
        except ValueError:
            print(integer_unused)

    return the_input

def instructions(the_content, message='Press any key in order to continue...'):
    """ To inform procedures of the algorithm. """
    the_instructions: str = f"""
    {the_content}
    """
    print(the_instructions)
    input(message)

def should_algorithm_run():
    input_text: str = f"""
    ========== Must the algorithm start running? ==========
    1 - Click after the arrow below
    2 - If YES, hit ENTER key
    3 - If NO, type "n" key and hit ENTER
    -> """
    return input_text

def welcome(algorithm_name: str):
    print(f'\nWelcome to the {colors[4]}{algorithm_name}{colors[7]}')
