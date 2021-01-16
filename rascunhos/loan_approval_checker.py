

"""
Requirements
------------

1. resources -> method to import variables and functions
"""

from resources import *

# Input variables in order of occurrence
input_algorithm_procedure: str = ''                # start()
input_house_price: float = 0.0                     # get_house_price()
input_salary_amount: float = 0.0                   # get_salary_amount()
input_years_to_pay: int = 0                        # get_years_to_pay()

person_thirty_percent_monthly_salary: float = 0.0  # calculate_financing_possibility()
percentage_thirty = 0.30                           # calculate_financing_possibility()
actual_monthly_cost: float = 0.0                   # calculate_financing_possibility()
total_months_per_year: int = 12                    # calculate_financing_possibility()

status: tuple = ()                                 # throw_result()
result_text: str = ''                              # throw_result()


steps: tuple = ('', '1. Should algorithm run?', '2. Display of instructions', '3. Provide input: price of the house',
                '4. Provide input: salary', '5. Provide input: years to pay', '6. Display of the result')

steps_colored: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n' for each_data in steps])


def custom_error(object_string):
    print(f"""
    {announcement}
    The {object_string} is invalid
    """)


def start():
    """To ask if algorithm must or not run. If user provides (str) 'end': break. Else: continues."""

    global input_algorithm_procedure

    print(steps_colored[1])

    input_algorithm_procedure = input(doubt_run_algorithm)


def instructions():
    """To inform procedures of the algorithm."""

    instructions_text: str = \
    f"""
    {steps_colored[2]}
    1. Provide: price of the house
    2. Provide: salary
    3. Provide: amount of years of payment intent
    4. It will be checked if your finances are suitable or not to start the loan"""

    print(instructions_text)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...


def get_house_price():
    """To treat improper data while a proper integer or floating number is not being provided."""

    global input_house_price

    input_text: str = \
    f"""
    {steps_colored[3]}
    {colors[0]}How much is the price of the house?{colors[7]} 
    1. {click_arrow}
    2. Inform an integer or non-integer value of the price of the house
    3. {press_enter_key}
    -> """

    while True:
        try:
            input_house_price = float(input(input_text))
            while input_house_price <= 0:           # while input = improper number
                custom_error('price of the house')  # throw this error function
                get_house_price()                   # repeat main function
            else:                                   # otherwise
                break                               # go to the next step
        except ValueError:                          # except if input = wrong type
            error_non_numerical_input()             # then throw this error funcion, loop repeats


def get_salary_amount():
    """To treat improper data while a proper integer or floating number is not being provided."""

    global input_salary_amount

    input_text: str = \
    f"""
    {steps_colored[4]}
    {colors[0]}How much is your salary?{colors[7]} 
    1. {click_arrow}
    2. Provide an integer of non-integer value of your salary
    3. {press_enter_key}
    -> """

    while True:
        try:
            input_salary_amount = float(input(input_text))
            while input_salary_amount <= 0.0:     # while input = improper number
                custom_error('salary')            # throw this error function
                get_salary_amount()               # repeat main function
            else:                                 # otherwise
                break                             # go to the next step
        except ValueError:                        # except if input = wrong type
            error_non_numerical_input()           # then throw this error funcion, loop repeats


def get_years_to_pay():
    """To treat improper data while a proper integer or floating number is not being provided."""

    global input_years_to_pay

    input_text: str = \
    f"""
    {steps_colored[5]}
    {colors[0]}For how many years will you pay?{colors[7]} 
    1. {click_arrow}
    2. Provide how many years the house will be paid
    3. {press_enter_key}
    -> """

    while True:
        try:
            input_years_to_pay = int(input(input_text))
            while input_years_to_pay <= 0:      # while input = improper number
                custom_error('amount of year')  # throw this error function
                get_years_to_pay()              # repeat main function
            else:                               # otherwise
                break                           # go to the next step
        except ValueError:                      # except if input = wrong type
            error_non_numerical_input()         # then throw this error funcion, loop repeats


def calculate_financing_possibility(salary: float = 1.0, house_price: float = 1.0, years_to_pay: int = 1):
    """To get client's 30% salary amount and how much the monthly payment is"""

    global person_thirty_percent_monthly_salary, percentage_thirty, actual_monthly_cost

    person_thirty_percent_monthly_salary = salary * percentage_thirty

    actual_monthly_cost = house_price / (total_months_per_year * years_to_pay)


def throw_result():
    """To build string of the result and use conditions to shape data and unpack them into the string"""

    global status, result_text

    status = (f'{colors[4]}loan allowed{colors[7]}', f'{colors[1]}loan denied{colors[7]}')

    frame: tuple = (steps_colored[6], input_house_price, input_salary_amount, input_years_to_pay,
                    person_thirty_percent_monthly_salary, actual_monthly_cost)

    result_text = \
    """
    {}
    ===================================
    # Price of the house:             # {} U$ dollars
    # Salary:                         # {} U$ dollars
    # Years to pay:                   # {} 
    # 30% percent of client's salary: # {:.2f} U$ dollars
    # Actual monthly cost:            # {:.2f} U$ dollars
    # Status:                         # {}
    ===================================
    """

    if person_thirty_percent_monthly_salary >= actual_monthly_cost:
        print(result_text.format(*frame, status[0]))
    else:
        print(result_text.format(*frame, status[1]))

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...

while True:
    welcome('Loan approval checker')
    start()
    if input_algorithm_procedure in algorithm_cease:
        print(closure)
        break
    instructions()
    get_house_price()
    get_salary_amount()
    get_years_to_pay()
    calculate_financing_possibility(input_salary_amount, input_house_price, input_years_to_pay)
    throw_result()
