# imports

import pytest
import arab2roman

# content of test_class.py
class TestClass:
    def test_exist(self):
        result = hasattr(int2roman, 'solution')
        assert result, "Function does not exist!"


        # is it converting correctly?
        # if you give it wrong input - text instead of number, decimal etc.
