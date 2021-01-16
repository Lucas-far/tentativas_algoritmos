

"""
Requirements
------------

1. OrderedDict -> method to use an ordered kind of dictionary
3. chdir       -> method to change to a specific path in a moment of the algorithm
4. resources   -> method to import variables and functions
"""

from collections import OrderedDict
from os import chdir
from resources import *

input_algorithm_procedure: str = ''      # start()

all_states_dict: dict = {}               # build_states_dict_and_str()
all_states_keys: list = []               # build_states_dict_and_str()
all_states_string: list = []             # build_states_dict_and_str()

input_state_id_number: int = 0           # get_state_id_number()

get_state_name: str = ''                 # collect_state_name()
state_name_keeper: list = []             # collect_state_name()

count_each_state_repetition: list = []   # count_each_state_repetition()
each_state_countage: str = ''            # count_each_state_repetition()

path_desktop: str = ''                   # register_result_into_file()
txt_file_label: str = ''                 # register_result_into_file()

steps: tuple = ('',
                '1. Should algorithm run?',
                '2. Provide: id number of your state',
                '3. Display of Visitors')

steps_painted: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n' for each_data in steps])


def start():
    """To ask if algorithm must or not run. If user provides (str) 'end': break. Else: continues."""

    global input_algorithm_procedure

    print(steps_painted[1])

    input_algorithm_procedure = input(doubt_run_algorithm)

def build_states_dict_and_str():
    """To create a dictonary of the states and place data into a string for a better display."""

    global all_states_dict, all_states_keys, all_states_string

    all_states_dict = OrderedDict({
        1: 'Acre', 2: 'Alagoas', 3: 'Amapá', 4: 'Amazonas', 5: 'Bahia',
        6: 'Brasília', 7: 'Ceará', 8: 'Espírito Santo', 9: 'Goiás', 10: 'Maranhão',
        11: 'Mato Grosso', 12: 'Mato Grosso do Sul', 13: 'Minas Gerais', 14: 'Paraíba', 15: 'Paraná',
        16: 'Pará', 17: 'Pernambuco', 18: 'Piauí', 19: 'Rio de Janeiro', 20: 'Rio Grande do Norte',
        21: 'Rio Grande do Sul', 22: 'Rondônia', 23: 'Roraima', 24: 'Santa Catarina', 25: 'São Paulo',
        26: 'Sergipe', 27: 'Tocantins'})

    all_states_string = \
    """
    {}  Acre               {}  Alagoas             {} Amapá            {}  Amazonas          {}  Bahia
    {}  Brasília           {}  Ceará               {} Espírito Santo   {}  Goiás             {}  Maranhão
    {} Mato Grosso        {} Mato Grosso do Sul  {} Minas Gerais    {} Paraíba           {} Paraná
    {} Pará               {} Pernambuco          {} Piauí           {} Rio de Janeiro    {} Rio Grande do Norte
    {} Rio Grande do Sul  {} Rondônia            {} Roraima         {} Santa Catarina    {} São Paulo
    {} Sergipe            {} Tocantins
    """.format(*all_states_dict.keys())

def get_state_id_number():
    """To treat improper data while a proper integer number is not being provided."""

    global input_state_id_number

    input_text = \
    f"""
    {steps_painted[2]}
    {colors[0]}What is the number of your state?{colors[7]} 
    1. {click_arrow}
    2. Type the integer number of your state
    3. {press_enter_key}
    -> """

    while True:
        try:
            print(all_states_string)  # to be reprinted everytime user makes a mistake
            input_state_id_number = int(input(input_text))
            while input_state_id_number <= 0 or input_state_id_number > 27:  # while input = improper number
                error_input_integer_out_of_range(1, 27)                      # throw this error function
                get_state_id_number()                                        # repeat main function
            else:                                                            # otherwise
                break                                                        # go to the next step
        except ValueError:                                                   # except if input = wrong type
            error_input_integer_not_used(1, 27)                              # then throw this error function, loop repeats

def collect_state_name():
    """To get an integer input and match with a dictionary key and program it to show its value, and place this value
     into a list."""

    global get_state_name, state_name_keeper

    get_state_name = all_states_dict.get(input_state_id_number)

    state_name_keeper.append(get_state_name)

def count_states():
    """To count separatedly all numbers of time a state has been placed in a list, and unpack the result into a string."""

    global count_each_state_repetition, each_state_countage

    count_each_state_repetition = [state_name_keeper.count(each_state) for each_state in all_states_dict.values()]

    # ========== TUTORIAL ==========
    # Assumption:     state_name_keeper = ['Acre', 'Tocantins']
    # count_each_state_repetition = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    each_state_countage = \
    """
    {}
    Acre:           {} visitor(s)    Alagoas:             {} visitor(s)     Amapá:              {} visitor(s) 
    Amazonas:       {} visitor(s)    Bahia:               {} visitor(s)     Brasília:           {} visitor(s)
    Ceará:          {} visitor(s)    Espírito Santo:      {} visitor(s)     Goiás:              {} visitor(s)
    Maranhão:       {} visitor(s)    Mato Grosso:         {} visitor(s)     Mato Grosso do Sul: {} visitor(s)
    Minas Gerais:   {} visitor(s)    Paraíba:             {} visitor(s)     Paraná:             {} visitor(s)
    Pará:           {} visitor(s)    Pernambuco:          {} visitor(s)     Piauí:              {} visitor(s)
    Rio de Janeiro: {} visitor(s)    Rio Grande do Norte: {} visitor(s)     Rio Grande do Sul:  {} visitor(s)
    Rondônia:       {} visitor(s)    Roraima:             {} visitor(s)     Santa Catarina:     {} visitor(s)
    São Paulo:      {} visitor(s)    Sergipe:             {} visitor(s)     Tocantins:          {} visitor(s)
    """.format(steps_painted[3], *count_each_state_repetition)

    print(each_state_countage)

def register_result_into_file():
    """To make a file and place the countage result into it."""

    global path_desktop, txt_file_label

    path_desktop = '/home/lucas/Desktop'

    chdir(path_desktop)

    txt_file_label = '\nReport of Visitor by state:\n'

    with open('visitors_by_state.txt', 'w') as doc:
        doc.write(txt_file_label)
        doc.write(str(each_state_countage))

while True:
    welcome('Visitor counter by state')
    start()
    if input_algorithm_procedure in algorithm_cease:
        print(closure)
        break
    build_states_dict_and_str()
    get_state_id_number()
    collect_state_name()
    count_states()
    register_result_into_file()
