import unittest

from hypothesis import example, given
from hypothesis.strategies import text

from reverse import reverse_string

class TestReverseHypothesis(unittest.TestCase):
  @given(text())
  def test_reversing_reversed_string_gives_original(self, a_str):
    assert a_str == reverse_string(reverse_string(a_str))

  @given(text())
  def test_reverse_string_equal_to_reverse(self, a_str):
    assert a_str[::-1] == reverse_string(a_str)