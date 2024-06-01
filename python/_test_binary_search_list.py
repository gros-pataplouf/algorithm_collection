import pytest
from binary_search_list import search

@pytest.fixture
def lst():
    return [1,2,3,4,5,6,7,8,9]

def test_returns_false_if_not_in_lst(lst):
    item = 0
    assert search(lst, item) == False

def test_returns_matching_item_if_in_lst(lst):
    item = 7
    assert search(lst, item) == 6

