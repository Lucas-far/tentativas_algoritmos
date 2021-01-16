

"""
Requirements
------------

1. resources -> module to import variables and functions
"""

from resources import *

input_algorithm_start: str = ''

input_temperature: float = 0.0

every_temperature_container: list = []

steps: tuple = ('', f'1 - Should algorithm run?', '2 - Display of Instructions', '3 - Provide input: temperature',
                '4 - Display of Result')

steps_painted: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n' for each_data in steps])


def start():
    """To ask if algorithm must or not run. If user provides (str) 'end': break. Else: continue."""

    global input_algorithm_start

    print(steps_painted[1])

    input_algorithm_start = input(doubt_run_algorithm)


def instructions():
    """To print procedures of the algorithm."""

    instructions_text: str = \
        f"""
    {steps_painted[2]}
    1. Provide input: temperature 
    2. The temperature input will be converted to other temperatures and displayed"""

    print(instructions_text)
    print(input(f'\n{colors[0]}Press any key to continue...{colors[7]}'))


def get_temperature():
    """To treat improper data while a proper integer number is not being provided."""

    global input_temperature

    input_text: str = \
        f"""
    {steps_painted[3]}
    {colors[0]}What temperature do you want to convert?{colors[7]}
    1 - {click_arrow}
    2 - Type any numerical temperature, either negative or positive
    3 - {press_enter_key}
    -> """

    error: str = \
        f"""
    {announcement}    
    The input is not of numerical type, therefore, invalid.
    """

    while True:
        try:
            input_temperature = float(input(input_text))
            break
        except ValueError:  # if input = wrong type
            print(error)    # throw this error print


def calculate_every_temperature(temperature):
    """To store each calculus of temperatures in a list"""

    global every_temperature_container

    every_temperature_container.append('{:.2f}'.format((temperature * 1.8) + 32))           # From celsius to fahrenheit
    every_temperature_container.append('{:.2f}'.format((temperature + 273.15)))             # From celsius to kelvin
    every_temperature_container.append('{:.2f}'.format((temperature - 32) * 5/ 9))  # From fahrenheit to celsius
    every_temperature_container.append(
        '{:.2f}'.format((temperature - 32) * 5 / 9 + 273.15))  # From fahrenheit to Kelvin
    every_temperature_container.append('{:.2f}'.format((temperature - 273.15)))  # From kelvin to celsius
    every_temperature_container.append('{:.2f}'.format((temperature - 273.15) * 1.8 + 32))  # From kelvin to fahrenheit


def throw_result():
    """"""

    result: str = \
    """
    {}
    Target temperature: {}

    ========== TABLE OF CONVERSION ===========

    From celsius to fahrenheit = {}°         
    From celsius to kelvin     = {}°         
    From fahrenheit to celsius = {}°         
    From fahrenheit to Kelvin  = {}°         
    From kelvin to celsius     = {}°         
    From kelvin to fahrenheit  = {}° 

    ==========================================
    """.format(steps_painted[4], input_temperature, *every_temperature_container)

    print(result)


while True:
    welcome('Tempeture converter')
    start()
    if input_algorithm_start in algorithm_cease:
        print(closure)
        break
    instructions()
    get_temperature()
    calculate_every_temperature(input_temperature)
    throw_result()
