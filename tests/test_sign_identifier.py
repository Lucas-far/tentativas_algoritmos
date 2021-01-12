

# from unittest import TestCase
#
# class Tests(TestCase):
#
#     def test_calculate_lifetime():
#         pass

def calculate_lifetime(year, month, day):
    """
    >>> calculate_lifetime(1992, 7, 16)
    'About 10406 days'
    """

    from datetime import datetime

    today = datetime.today()

    the_birthday = datetime(year=year, month=month, day=day)
    the_birthday_srt = f'{year}/{month}/{day}'
    the_existence_calculus = today - the_birthday
    the_result = f'About {str(the_existence_calculus).split()[0]} days'

    "Example"  # the_existence_calculus = 2020/07/08 - 1992/7/16 = 10219 days, 23:33:12.115426
    "Example"  # result = About 10219 days

    return the_result

def customize_birthday(year: int = 1, month: int = 1, day: int = 1, the_result=None):
    """
    >>> customize_birthday(2020, 7, 16)
    datetime.datetime(2020, 7, 16, 0, 0)
    """

    from datetime import datetime
    the_birthday = datetime(year=year, month=month, day=day)
    return the_birthday

def customize_birthday_str(year: int = 1, month: int = 1, day: int = 1, the_result=None):
    """
    >>> customize_birthday_str(1992, 7, 16)
    '1992/7/16'
    """
    the_result = f'{year}/{month}/{day}'
    return the_result
