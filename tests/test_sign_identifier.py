

from unittest import TestCase

from methods_database import (
    calculate_lifetime, customize_birthday, customize_birthday_str, find_sign, get_input_integer, instructions,
    input_printer, should_algorithm_run, step_painter, welcome
)

"Run all tests at once"  # python -m unittest discover tests

class TestCalculateLifetime(TestCase):

    def setUp(self) -> None:
        self.test_var = calculate_lifetime(year=1992, month=7, day=16)    # About 10426 days

    def test_calculate_lifetime(self) -> None:
        self.assertEqual(calculate_lifetime(1992, 7, 16), self.test_var)  # About 10426 days == About 10426 days
        self.assertNotEqual(calculate_lifetime(), self.test_var)          # About 737820 days != About 10426 days

class TestCustomizeBirthday(TestCase):

    def setUp(self) -> None:
        self.test_var = customize_birthday(year=1992, month=7, day=16)  # 1992-07-16 00:00:00

    def test_customize_birthday(self) -> None:
        self.assertEqual(customize_birthday(1992, 7, 16), self.test_var)  # 1992-07-16 == 1992-07-16
        self.assertNotEqual(customize_birthday(), self.test_var)          # 0001-01-01 != 1992-07-16

class TestCustomizeBirthdayStr(TestCase):

    def setUp(self) -> None:
        self.test_var = customize_birthday_str(1992, 7, 16)

    def test_customize_birthday_str(self) -> None:
        self.assertEqual(customize_birthday_str(1992, 7, 16), self.test_var)
        self.assertNotEqual(customize_birthday_str(), self.test_var)

"1"  # This method (def find_sign) does not exactly rely on other methods, but it is a good idea to use others
"2"  # Because parameters: (birthday) (existence) are result of calculus, which are converted to strings
"3"  # Strings could be passed, simulating the results, but I would not want to pass random fake results
"4"  # This is way I decided to call other functions, in order to create genuine values
class TestFindSign(TestCase):

    def setUp(self) -> None:
        self.birthday_str = customize_birthday_str(1992, 7, 16)   # created to avoid literal strings in the parameters
        self.lifetime = calculate_lifetime(1992, 7, 16)           # idem (samething)
        self.test_var = find_sign(birthday=self.birthday_str, existence=self.lifetime, month=7, day=16)

    def test_find_sign(self) -> None:
        self.assertEqual(find_sign(birthday=self.birthday_str, existence=self.lifetime, month=7, day=16), self.test_var)
        self.assertNotEqual(find_sign(), self.test_var)

class TestGetInputInteger(TestCase):
    def setUp(self) -> None:
        self.test_var = get_input_integer(the_input=7)                       # 7
        # self.test_var2 = get_input_integer()

    def test_get_input_integer(self) -> None:
        self.assertEqual(get_input_integer(the_input=7), self.test_var)      # 7 == 7
        self.assertNotEqual(get_input_integer(the_input=10), self.test_var)  # 7 == 10

class TestInstructions(TestCase):
    def setUp(self) -> None:
        self.test_var = instructions()  # Indefinido

    def test_instructions(self) -> None:
        self.assertEqual(instructions('Indefinido'), self.test_var)
        self.assertNotEqual(instructions('Procedures'), self.test_var)

class TestInputPrinter(TestCase):
    def setUp(self) -> None:
        self.test_var = input_printer()                     # Press any key...
        self.test_var2 = input_printer('Press any key...')  # Press any key...
        self.test_var3 = 'ok'                               # ok

    def test_input_printer(self) -> None:
        self.assertEqual(self.test_var, self.test_var2)
        self.assertNotEqual(self.test_var2, self.test_var3)

class TestShouldAlgorithmRun(TestCase):
    def setUp(self) -> None:
        self.test_var = should_algorithm_run()
        self.test_var2 = 'undefined'

    def test_should_algorithm_run(self):
        self.assertEqual(should_algorithm_run(), self.test_var)
        self.assertNotEqual(self.test_var, self.test_var2)

class TestStepPainter(TestCase):
    def setUp(self) -> None:
        self.test_var = step_painter('a', 'b', 'c', prefix=0, prefix2=7)

    def test_step_painter(self):
        self.assertEqual(step_painter('a', 'b', 'c'), self.test_var)
        self.assertNotEqual(step_painter('Step 1', 'Step 2', prefix=4, prefix2=7), self.test_var)

class TestWelcome(TestCase):
    def setUp(self) -> None:
        self.test_var = welcome()                          # Welcome to the Name of the algorithm
        self.test_var2 = welcome('Name of the algorithm')  # Welcome to the Name of the algorithm
        self.test_var3 = welcome('Sign Identifier')        # Welcome to the Sign Identifier

    def test_welcome(self):
        self.assertEqual(self.test_var, self.test_var2)      # Welcome to the Name of the algorithm == Welcome to the Name of the algorithm
        self.assertNotEqual(self.test_var2, self.test_var3)  # Welcome to the Name of the algorithm != Welcome to the Sign Identifier
