import pytest
from has_valid_brackets import has_valid_brackets


def test_has_valid_brackets1():
   assert has_valid_brackets("p()")

def test_has_valid_brackets2():
   assert not has_valid_brackets("][a")

def test_has_valid_brackets3():
   assert has_valid_brackets("{[z]{d()}}")

def test_has_valid_brackets4():
   assert has_valid_brackets("{}[]()")

def test_has_valid_brackets5():
   assert has_valid_brackets("{[(([{}]))]}")