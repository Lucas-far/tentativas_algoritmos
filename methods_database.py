

""""""
from datetime import datetime

def calculate_lifetime(year: int = 1, month: int = 1, day: int = 1) -> str:
    """
    To calculate user life time and return the result as custom string
    :param year:
    :param month:
    :param day:
    :return: str
    """
    today = datetime.today()

    the_birthday = datetime(year=year, month=month, day=day)
    the_existence_calculus = today - the_birthday
    the_result = f'About {str(the_existence_calculus).split()[0]} days'

    "Example"  # the_existence_calculus = 2020/07/08 - 1992/7/16 = 10219 days, 23:33:12.115426
    "Example"  # result = About 10219 days

    return the_result

def customize_birthday(year: int = 1, month: int = 1, day: int = 1) -> datetime:
    """
    To build a datetime data through integers
    :param year:
    :param month:
    :param day:
    :return datetime
    """

    the_birthday = datetime(year=year, month=month, day=day)

    return the_birthday

def customize_birthday_str(year: int = 1, month: int = 1, day: int = 1) -> str:
    """
    To build an american date pattern through integers
    :param year:
    :param month:
    :param day:
    :return: str
    """
    the_result = f'{year}/{month}/{day}'
    return the_result

def find_sign(birthday: str = 'Absent', existence: str = 'Absent', existing_signs: int = 12, day: int = 1, month: int = 1) -> str:
    """
    To find between numeric tuples, which ones match with user's month and day of birth and place result into a string
    :param birthday:
    :param existence:
    :param existing_signs:
    :param day:
    :param month:
    :return: str
    """

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
        'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Saggitarius'
    )

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

def get_input_integer(the_input: int, input_text: str = 'Write an integer -> ', the_initial_integer: int = 1, the_last_integer: int = 9999) -> int:
    """
    To treat improper data while a proper integer number is not being provided.
    :param the_input:
    :param input_text:
    :param the_initial_integer:
    :param the_last_integer:
    :return: int
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

def instructions(content: str) -> str:
    """
    To inform procedures of an algorithm.
    :param content:
    :return: str
    """
    the_instructions = f"""
    {content}
    """
    return the_instructions

def input_printer(message: str = 'Press any key in order to continue...') -> input:
    """
    To return an input with a message of instruction, and to control code rolling, if there is/are other inputs
    :param message:
    :return:
    """
    return input(message)

def should_algorithm_run() -> str:
    """
    To return a string suitable to start an algorithm, to ask if it must or not run
    :return: str
    """

    text = f"""
    ========== Must the algorithm start running? ==========
    1 - Click after the arrow below
    2 - If YES, hit ENTER key
    3 - If NO, type "n" key and hit ENTER
    -> """

    return text

def step_painter(*args, prefix=0, prefix2=7) -> tuple:
    """
    To store texts into a tuple and alter the standard color of the IDE
    :param args:
    :param prefix: goes from 0 to 6, and combine with prefix2, frozen as 7. EX: prefix = 0 & prefix2 = 7 = black
    :param prefix2: must always be 7, if it is desired colors to work
    :return: tuple
    """
    pallet: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    steps = tuple([f'\n{pallet[prefix]}{step}{pallet[prefix2]}\n' for step in args])

    return tuple(steps)

def welcome(algorithm_name: str = 'Name of the algorithm', prefix: int = 0, prefix2: int = 7) -> str:
    """
    To receive a string and return it as the name of the algorithm
    :param algorithm_name:
    :param prefix: goes from 0 to 6, and combine with prefix2, frozen as 7. EX: prefix = 0 & prefix2 = 7 = black
    :param prefix2: must always be 7, if it is desired colors to work
    :return: str
    """

    pallet: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    return f'\nWelcome to the {pallet[prefix]}{algorithm_name}{pallet[prefix2]}'

if __name__ == '__main__':
    pass
