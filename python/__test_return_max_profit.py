import pytest
from stock_max_profit import profit

@pytest.fixture
def array_no_max():
    return [1,1,1,1,1,1,1]

@pytest.fixture
def array_ascending():
    return [1,2,3,4,5,6,7]

@pytest.fixture
def array_descending():
    return [7,6,5,4,3,2,1]

@pytest.fixture
def array_one_peak():
    return [1,2,3,4,3,2,1]

@pytest.fixture
def array_one_slump():
    return [4,3,2,1,1,2,3,5]

@pytest.fixture
def array_several_peaks():
    return [9,2,6,5,4,7,3,9,10,5]


def test_profit_0_if_no_max(array_no_max):
    assert profit(array_no_max) == 0

def test_ascending_delta(array_ascending):
    ind = 0
    delta = 0
    min = 0
    max = 0
    for price in array_ascending:
        if ind == 0:
            min = price
        if min > price:
            min = price
        if max < price:
            max = price
        ind += 1
    delta = max - min
    assert profit(array_ascending) == delta

def test_descending_delta(array_descending):
    assert profit(array_descending) == 0

def test_array_one_peak(array_one_peak):
    assert profit(array_one_peak) == 3

def test_array_with_one_slump(array_one_slump):
    assert profit(array_one_slump) == 4

def test_array_several_peaks(array_several_peaks):
    assert profit(array_several_peaks) == 8
