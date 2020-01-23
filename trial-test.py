# imports

import pytest
import int2roman

# content of test_class.py
class TestClass:
    def test_exist(self):
        result = hasattr(int2roman, 'int_to_Roman')
        assert result, "Function does not exist!"
    def test_int(self):
        result = problem4.int_to_Roman(10)
        self.assertTrue((isinstance(result, int)))
    def test_neg(self):
        result = problem4.int_to_Roman(-10)
        self.assertFalse((isinstance(result, int)))
    def test_str(self):
        result = problem4.int_to_Roman(s)
        self.assertFalse((isinstance(result, int)))
    def test_random(self):
        result = problem4.int_to_Roman(s8109sjn-)
        self.assertFalse((isinstance(result, int)))           # is it converting correctly?
        # if you give it wrong input - text instead of number, decimal etc.
