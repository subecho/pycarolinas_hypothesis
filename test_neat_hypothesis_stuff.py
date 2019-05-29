import logging

from hypothesis import given
from hypothesis.strategies import builds, integers, lists, sampled_from, text

log = logging.getLogger("log")

# We can use the builds() strategy to get something from a callable and arguments
@given(builds(iter, lists(integers())))
def test_dictionary_construction(iterator):
  log.info("Starting Iteration")
  for item in iterator:
    log.info(item)
  log.info("Stopping Iteration")

# We can also generate arbitrary lists using other strategies.
@given(lists(text(), min_size=10, max_size=100))
def test_lists_can_have_a_lot_of_strings(str_list):
  for string in str_list:
    log.info(string)

# Let's make an object...
class Person(object):
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age
  
  def __str__(self):
    return "Hi, I'm {} and I'm {}.".format(self.name, self.age)

# And use it in our tests (remember, constructors are just callables too!)
@given(builds(Person, text(), integers()))
def test_create_person(a_person):
  log.info(a_person)