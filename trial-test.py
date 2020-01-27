

import pytest
import int2roman

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

# content of test_class.py
class TestClass:
    def test_correct(self):
        result = int2roman.int_to_Roman(4)
        assert result == "IV"
    def test_wrong(self):
        result = int2roman.int_to_Roman(4)
        assert result != "I"
