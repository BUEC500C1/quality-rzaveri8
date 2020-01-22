# imports

import pytest
import arab2roman

# content of test_class.py
class TestClass:
    def test_parser_does_exist(self):
        result = hasattr(arab2roman, 'solution')
        assert(result, "Function does not exist!")
