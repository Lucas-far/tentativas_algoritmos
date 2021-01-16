

"""
Requirements
------------
1. resources      (type=module) to import variables and functions
"""

from resources import *

input_algorithm_start: str = ''          # start()
input_perfume_number: int = 0            # get_perfume_id()
input_payment_method: int = 0            # get_payment_method()
input_number_installments: int = 0       # get_number_installments()

products_dict: dict = {}                 # make_dictionary_of_products()
each_perfume_price: list = []            # make_dictionary_of_products()
products_str: str = ''                   # make_dictionary_of_products()

perfume_name: str = ''                   # get_perfume_data(id_perfume: int = 0)
perfume_source_price: float = 0.0        # get_perfume_data(id_perfume: int = 0)

percentage_ten: float = 0.10             # calculate_discount_and_rise(original_price: float = 0.0)
percentage_fifteen: float = 0.15         # calculate_discount_and_rise(original_price: float = 0.0)
discount: float = 0.0                    # calculate_discount_and_rise(original_price: float = 0.0)
rise: float = 0.0                        # calculate_discount_and_rise(original_price: float = 0.0)
perfume_price_allcash: float = 0.0       # calculate_discount_and_rise(original_price: float = 0.0)
perfume_price_parceled_out: float = 0.0  # calculate_discount_and_rise(original_price: float = 0.0)

primary_result_text: str = ''            # throw_primary_result()

price_per_installment: float = 0.0       # throw_secondary_result()
secondary_result_text: str = ''          # throw_secondary_result()

steps: tuple = ('',
                '1. Should algorithm run?',
                '2. Display of instructions',
                '3. Display of products',
                '4. Provide input: perfume id/number',
                '5. Report of the chosen product',
                '6. Provide input: payment method',
                '7. Report: allcash payment',
                '7. Provide input: number of installments',
                '8. Report: parceled_out payment')

steps_colored: tuple = tuple([f'\n{colors[2]}{each_data}{colors[7]}\n' for each_data in steps])


def start():
    """To ask if algorithm must or not run. If user provides (str) 'end': break. Else: continues."""

    global input_algorithm_start

    print(steps_colored[1])

    input_algorithm_start = input(doubt_run_algorithm)


def instructions():
    """To inform procedures of the algorithm."""

    instructions_text: str = \
    f"""
    {steps_colored[2]}
    1. Products will be displayed
    2. The price of the products are provisory
    3. The prices exchange based on the provided payment choice
    4. If payment choice is allcash, source price - 10%
    5. If payment choice is parceled out, source price + 15% 
    """

    print(instructions_text)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...


def make_dictionary_of_products():
    """To display a dictionary informing data regarding the products"""

    global products_dict, each_perfume_price, products_str

    products_dict = {
        1: {'perfume': 'Alfond', 'price': 114.19}, 2: {'perfume': 'Bistrax', 'price': 327.02},
        3: {'perfume': 'Calak', 'price': 437.91}, 4: {'perfume': 'Dontrag', 'price': 459.13},
        5: {'perfume': 'Ecbas', 'price': 156.47}, 6: {'perfume': 'Furonja', 'price': 113.09},
        7: {'perfume': 'Gatika', 'price': 443.12}, 8: {'perfume': 'Hyna', 'price': 68.14},
        9: {'perfume': 'Iutru', 'price': 490.99}, 10: {'perfume': 'Janax', 'price': 92.48},
        11: {'perfume': 'Kiusko', 'price': 463.22}, 12: {'perfume': 'Lemika', 'price': 92.53},
        13: {'perfume': 'Moswa', 'price': 463.07}, 14: {'perfume': 'Natra', 'price': 481.08},
        15: {'perfume': 'Okixa', 'price': 134.26}, 16: {'perfume': 'Pelva', 'price': 273.73},
        17: {'perfume': 'Quantre', 'price': 35.66}, 18: {'perfume': 'Ravna', 'price': 203.97},
        19: {'perfume': 'Siuza', 'price': 256.31}, 20: {'perfume': 'Tenki', 'price': 22.05},
        21: {'perfume': 'Uyato', 'price': 442.67}, 22: {'perfume': 'Vaki', 'price': 440.88},
        23: {'perfume': 'Woltre', 'price': 485.81}, 24: {'perfume': 'Xiahu', 'price': 4.99},
        25: {'perfume': 'Yaja', 'price': 214.49}
    }

    each_perfume_price = [products_dict.get(each_perfume)['price'] for each_perfume in products_dict]

    products_str = \
    """
    1.  Alfond [{}]     2. Bistrax [{}]     3. Calak [{}]      4. Dontrag [{}]     5. Ecbas [{}]    
    6.  Furonja [{}]    7. Gatika [{}]      8. Hyna [{}]        9. Iutru [{}]      10. Janax [{}]
    11. Kiusko [{}]    12. Lemika [{}]      13. Moswa [{}]     14. Natra [{}]      15. Okixa [{}]
    16. Pelva [{}]     17. Quantre [{}]     18. Ravna [{}]     19. Siuza [{}]      20. Tenki [{}]
    21. Uyato [{}]     22. Vaki [{}]       23. Woltre [{}]    24. Xiahu [{}]        25. Yaja [{}]""".format(*each_perfume_price)

    print(products_str)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...


def get_perfume_id():
    """To treat improper data while a proper integer number is not being provided."""

    global input_perfume_number

    input_text: str = \
    f"""
    {steps_colored[4]}
    {colors[0]}What is the id of the perfume to be searched a discount?{colors[7]} 
    1. {click_arrow}
    2. Type the number of the perfume [ 1 to 25 ]
    3. {press_enter_key}
    -> """

    while True:

        try:
            print(steps_colored[3])
            make_dictionary_of_products()
            input_perfume_number = int(input(input_text))
            while input_perfume_number <= 0 or input_perfume_number > 25:  # while input = improper number
                error_input_integer_out_of_range(1, 25)                    # throw this error function
                get_perfume_id()                                           # repeat main function
            else:                                                          # otherwise
                break                                                      # go to the next step
        except ValueError:                                                 # except if input = wrong type
            error_input_integer_not_used(1, 25)                            # then throw this error function, loop repeats


def get_perfume_data(id_perfume: int = 0):
    """To extract from the id, the name and price of the product"""

    global perfume_name, perfume_source_price

    perfume_name = products_dict.get(id_perfume)['perfume']

    perfume_source_price = products_dict.get(id_perfume)['price']

    product_database: str = \
    f"""
    {steps_colored[5]}
    ==================
    // Id           // {colors[0]}{input_perfume_number}{colors[7]} 
    // Name         // {colors[0]}{perfume_name}{colors[7]}
    // Source price // {colors[0]}{perfume_source_price}{colors[7]}
    ==================
    """

    print(product_database)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...


def get_payment_method():
    """To treat improper data while a proper integer number is not being provided."""

    global input_payment_method

    input_text: str = \
    f"""
    {steps_colored[6]}
    {colors[0]}What payment choice do you pick?{colors[7]} 
    1. {click_arrow}
    - Type 0 for allcash payment method
    - Type 1 for parceled out payment method
    2. {press_enter_key}
    -> """

    while True:

        try:
            input_payment_method = int(input(input_text))
            while input_payment_method < 0 or input_payment_method > 1:  # while input = improper number
                error_input_integer_out_of_range(0, 1)                   # throw this error function
                get_payment_method()                                     # repeat main function
            else:                                                        # otherwise
                break                                                    # go to the next step
        except ValueError:                                               # except if input = wrong type
            error_input_integer_not_used(0, 1)                           # then throw this error function, loop repeats


def calculate_discount_and_rise(original_price: float = 0.0):
    """To alter source price based on payment method"""

    global percentage_ten, percentage_fifteen, discount, rise, perfume_price_allcash, perfume_price_parceled_out

    discount = original_price * percentage_ten

    rise = original_price * percentage_fifteen

    perfume_price_allcash = original_price - discount

    perfume_price_parceled_out = original_price + rise


def throw_primary_result():
    """To print a report in case of allcash payment method chosen"""

    global primary_result_text

    frame: tuple = (perfume_name, perfume_source_price, perfume_price_allcash, colors[3], discount, colors[7])

    primary_result_text = \
    """
    {}
    ======================
    // 1. Product name  // [ {} ]                                                                                            
    // 2. Source price  // U$ [ {:.2f} ]                                                                              
    // 3. Allcash price // U$ [ {:.2f} ]                                                                              
    // 4. Discount      // U$ [ {}{:.2f}{} ] 
    ======================                                                                         
    """.format(steps_colored[7], *frame)

    print(primary_result_text)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...


def get_number_installments():
    """To treat improper data while a proper integer number is not being provided."""

    global input_number_installments

    input_text: str = \
    f"""
    {steps_colored[8]}
    {colors[0]}What is the number of installments to be split?{colors[7]} 
    1. {click_arrow}
    2. Type the number of installments [ 2 to 9 ]
    3. {press_enter_key}
    -> """

    while True:
        try:
            input_number_installments = int(input(input_text))
            while input_number_installments < 2 or input_number_installments > 9:  # while input = improper number
                error_input_integer_out_of_range(2, 9)                             # throw this error function
                get_number_installments()                                          # repeat main function
            else:                                                                  # otherwise
                break                                                              # go to the next step
        except ValueError:                                                         # except if input = wrong type
            error_input_integer_not_used(2, 9)                                     # then throw this error function, loop repeats


def throw_secondary_result():
    """To print a report in case of parceled out payment method"""

    global price_per_installment, secondary_result_text

    price_per_installment = perfume_price_parceled_out / input_number_installments

    frame: tuple = (perfume_name, perfume_source_price, perfume_price_parceled_out, colors[1], rise, colors[7],
                    input_number_installments, price_per_installment)

    secondary_result_text = \
    """
    {}
    ==============================
    // 1. Name of the product   // [ {} ]
    // 2. Source price          // U$ [ {:.2f} ]
    // 3. Parceled out price    // U$ [ {:.2f} ] 
    // 4. Rise                  // U$ [ {}{:.2f}{} ]
    // 5. Number of installmens // U$ [ {} ]
    // 6. Price per installment // U$ [ {:.2f} ] each
    ==============================
    """.format(steps_colored[9], *frame)

    print(secondary_result_text)

    input(f'\n{colors[0]}Press ANY KEY to continue...{colors[7]}\n')  # to prevent next content scrolling...


while True:
    welcome('Discount calculator')
    start()
    if input_algorithm_start in algorithm_cease:  # if user provides 'end' = end of the algorithm
        print(closure)
        break
    instructions()
    get_perfume_id()
    get_perfume_data(input_perfume_number)
    get_payment_method()
    calculate_discount_and_rise(perfume_source_price)
    while True:
        if input_payment_method == 0:
            throw_primary_result()
            break
        else:
            get_number_installments()
            throw_secondary_result()
            break
