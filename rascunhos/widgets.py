

colors: tuple = ('\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m')
announcement: str = f'\n{colors[1]}========== ERROR =========={colors[7]}\n'
algorithm_closure: tuple = ('n',)
algorithm_cease: tuple = ('end',)
scroll_down: str = "Press ENTER to scroll down to the next content"
click_arrow: str = 'Click after the arrow below'
press_enter_key: str = 'Press ENTER'
closure: str = f'{colors[1]}\nAlgorithm has been successfuly shut down{colors[7]}'
instruction = f'\n{colors[2]}Press ENTER to continue{colors[7]}\n'

def welcome(algorithm_name: str):
    print(f'\nWelcome to the {colors[4]}{algorithm_name}{colors[7]}')

def should_algorithm_run():
    step_one = '1 - Click after the arrow below'
    step_two = '2 - If YES, hit ENTER key'
    step_three = '3 - If NO, type "n" key and hit ENTER'
    input_text: str = f"""
    ========== Must the algorithm start running? ==========
    {step_one}
    {step_two}
    {step_three}
    -> """
    return input_text

def error_input_integer_out_of_range(first_value, last_value):
    print(f"""
    {announcement}
    The provided input is not in the suitable range: {first_value} to {last_value}
    """)

def error_input_floating_out_of_range(first_value: float = 0.0, last_value: float = 0.0):
    print(f"\n{announcement}\nThe provided input is not in the suitable range: {first_value} to {last_value}")

def error_input_integer_not_used(first_value, last_value):
    print(f"""
    {announcement}
    The provided input must be an integer number: {first_value} to {last_value}
    """)

def error_input_floating_not_used(first_value, last_value):
    print(f"\n{announcement}\nThe provided input must be a floating number: {first_value} to {last_value}")

def error_non_integer_input():
    print(f"""
    {announcement}
    The input provided does not seem to be only an integer value
    {colors[1]}Avoid:{colors[7]} integer numbers with special characters
    """)

def error_non_numerical_input():
    print(f"""
    {announcement}
    {colors[0]}The input provided does not seem to be only numerical{colors[7]}
    {colors[0]}If input is an integer:{colors[7]} {colors[3]}You can only use underline to separate numbers with 4+ digits{colors[7]}
    {colors[0]}If input is non-integer:{colors[7]} {colors[3]}You can use underline to separate integer fields and dot to separate decimal fields{colors[7]}
    """)
