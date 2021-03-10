

from utils.widgets import click_arrow, hit_enter

inks: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

instructions_text = f"""
    ========== INSTRUCTIONS ==========
    1 - Provide your {inks[1]}birth day{inks[7]}
    2 - Provide your {inks[1]}birth month{inks[7]}
    3 - Provide your {inks[1]}birth year{inks[7]}
    4 - The algorithm will return user's sign and lifetime existence
    """

input_text_which_day = f"""
    ======= QUESTION: {inks[0]}In what day have you been born?{inks[7]} =======
    1 - {click_arrow}
    2 - Type the day you have been born (from 1 to 31)
    3 - {hit_enter}
    -------> """

input_text_which_month = f"""
    ======= QUESTION: {inks[0]}In what month have been born?{inks[7]} =======
    1 - {click_arrow}
    2 - Type the month you have been born (from 1 to 12)
    3 - {hit_enter}
    -------> """

input_text_which_year = f"""
    ======= QUESTION: {inks[0]}In what year have you been born?{inks[7]} =======
    1 - {click_arrow}
    2. Type the year you have been born (from year 1 to 9999)
    3 - {hit_enter}
    -------> """
