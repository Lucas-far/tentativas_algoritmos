

colors: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

algorithm_closure: tuple = ('n',)
the_breaking_point: tuple = ('n',)
click_arrow: str = 'Click after the arrow below'
hit_enter: str = 'Press ENTER key'
the_closure: str = f'{colors[1]}\nAlgorithm has been shut down{colors[7]}'

# def error_input_floating_out_of_range(first_value: float = 0.0, last_value: float = 0.0):
#     print(f"\n{announcement}\nThe provided input is not in the suitable range: {first_value} to {last_value}")
#
# def error_input_floating_not_used(first_value, last_value):
#     print(f"\n{announcement}\nThe provided input must be a floating number: {first_value} to {last_value}")
#
# def error_non_integer_input():
#     print(f"""
#     {announcement}
#     The input provided does not seem to be only an integer value
#     {colors[1]}Avoid:{colors[7]} integer numbers with special characters
#     """)
#
# def error_non_numerical_input():
#     print(f"""
#     {announcement}
#     {colors[0]}The input provided does not seem to be only numerical{colors[7]}
#     {colors[0]}If input is an integer:{colors[7]} {colors[3]}You can only use underline to separate numbers with 4+ digits{colors[7]}
#     {colors[0]}If input is non-integer:{colors[7]} {colors[3]}You can use underline to separate integer fields and dot to separate decimal fields{colors[7]}
#     """)
