

import pytest
import int2roman

# content of test_class.py
class TestClass:
    def test_exist(self):
        result = hasattr(int2roman, 'int_to_Roman')
        assert result, "Function does not exist!"
    def test_correct(self):
        result = int2roman.int_to_Roman(4)
        assert result == "IV"
    def test_correct(self):
        result = int2roman.int_to_Roman(70000)
        assert result == "LXX"
    def test_correct(self):
        result = int2roman.int_to_Roman(99999)
        assert result == "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCMXCIX"
    def test_neg(self):
        result = int2roman.int_to_Roman(-4)
        assert result == "ERROR: Not a positive integer"
    def test_string(self):
        result = int2roman.int_to_Roman('hello')
        assert result == "ERROR: Not an integer"
    def test_value(self):
        result = int2roman.int_to_Roman(8910394)
        assert result == "Enter a valid Roman Numeral or Integer from 1 to 99999"


"""
    def test_exist(self):
        result = hasattr(int2roman, 'int_to_Roman')
        assert result, "Function does not exist!"
    def test_int(self):
        result = int2roman.int_to_Roman(10)
        self.assertEqual((isinstance(result, 'X')))
    def test_neg(self):
        result = int2roman.int_to_Roman(-10)
        self.assertFalse((isinstance(result, int)))
    def test_str(self):
        result = int2roman.int_to_Roman(s)
        self.assertFalse((isinstance(result, int)))
    def test_random(self):
        result = int2roman.int_to_Roman(s8109sjn-)
        self.assertFalse((isinstance(result, int)))           # is it converting correctly?
        # if you give it wrong input - text instead of number, decimal et
"""
"""
class TestClass:

    def test_function_1(self):
        # Override the Python built-in input method
        int2roman.raw_input = lambda: int2roman.inputNumber(3)
        # Call the function you would like to test (which uses input)
        output = int2roman.int_to_roman(3)
        assert output == 'III'

    def test_function_2(self):
        module.input = lambda: 'some_other_input'
        output = module.function()
        assert output == 'another_expected_output'

    def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
       module.input = input

         """
