

"""
Methods used on the algorithm, which have already been tested

-> get_input_integer at [ test_sign_identifier.py ]
-> input_printer     at [ test_sign_identifier.py ]
-> instructions      at [ test_sign_identifier.py ]
-> welcome           at [ test_sign_identifier.py ]
-> step_painter      at [ test_sign_identifier.py ]
"""

from unittest import TestCase
from methods_database import (
    number_maker_by_difficulty, calculus_printer, operator_finder, math_maker, tell_if_this_basic_math_true,
    message_frame
)

"Run all tests at once"  # python -m unittest discover tests

"Model to save time"
# class Test(TestCase):
#
#     def setUp(self) -> None:
#         self.test_var = None
#         self.test_var2 = None
#
#     def test_(self):
#         self.assertEqual()
#         self.assertNotEqual()

class TestNumberMakerByDifficulty(TestCase):

    def setUp(self) -> None:
        self.test_var, self.test_var2 = number_maker_by_difficulty()                        # 0, 0
        # var below in its pattern, generates any integer between 1 to 9
        self.test_var3 = number_maker_by_difficulty(alternative=False, alternative2=False)  # 7

    def test_number_maker_by_difficulty(self) -> None:
        self.assertEqual(0, self.test_var)                   # 0 == 0
        self.assertEqual(0, self.test_var2)                  # 0 == 0
        self.assertNotEqual(self.test_var, self.test_var3)   # 0 != 7
        self.assertNotEqual(self.test_var2, self.test_var3)  # 0 != 7

class TestCalculusPrinter(TestCase):

    def setUp(self) -> None:
        self.test_var = calculus_printer()  # 1 + 1?
        self.test_var2 = calculus_printer(value_one=2, value_two=2, alternative_operator=False)
        "ex"      # self.test_var2 = ========== Quanto é 2 - 2? ==========
        "detail"  # self.test_var2 can switch between operators: +, - or x

    def test_calculus_printer(self) -> None:
        self.assertEqual('1 + 1?', self.test_var)            # 1 + 1? == 1 + 1?
        self.assertNotEqual(self.test_var2, self.test_var)   # ========== Quanto é 2 - 2? ========== != 1 + 1?

class TestOperatorFinder(TestCase):

    def setUp(self) -> None:
        self.test_var = operator_finder()                                      # **
        self.test_var2 = operator_finder('1 + 1', alternative_operator=False)  # +

    def test_operator_finder(self) -> None:
        self.assertEqual('**', self.test_var)               # ** == **
        self.assertNotEqual(self.test_var2, self.test_var)  # + != **

class TestMathMaker(TestCase):

    def setUp(self) -> None:
        self.test_var = math_maker()                   # None
        self.test_var2 = math_maker(the_operator='x')  # 1

    def test_math_maker(self) -> None:
        self.assertEqual(None, self.test_var)               # None == None
        self.assertNotEqual(self.test_var2, self.test_var)  # 1 != None

class TestTellIfThisBasicMathTrue(TestCase):

    def setUp(self) -> None:
        self.test_var = tell_if_this_basic_math_true()                                 # None
        self.test_var2 = tell_if_this_basic_math_true(the_operator='+', the_result=2)  # True

    def test_tell_if_this_basic_math_true(self):
        self.assertEqual(None, self.test_var)               # None == None
        self.assertNotEqual(self.test_var, self.test_var2)  # None != True

class TestMessageFrame(TestCase):

    def setUp(self) -> None:
        self.test_var = message_frame()  # ----- MENSAGEM -----
        self.test_var2 = message_frame('MENSAGEM')

    def test_message_frame(self):
        self.assertEqual('----- MENSAGEM -----', self.test_var)  # ----- MENSAGEM ----- == ----- MENSAGEM -----
        self.assertNotEqual(self.test_var, self.test_var2)       # ----- MENSAGEM ----- != MENSAGEM
