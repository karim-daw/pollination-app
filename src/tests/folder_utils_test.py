""" example of test module in pytest"""

from folder_utils import total
from folder_utils import convertArgsToStrings
from folder_utils import convertKeyValueToString

# total
def test_total_empty() -> None:
    """ Total of empty list should be 0.0"""
    assert total([]) == 0.0

def test_total_single_item() -> None:
    assert total([110.0]) == 110.0

def test_total_many_item() -> None:
    assert total([110.0,2.0,3.0]) == 115.0

# convertArgsToStrings
def test_convertArgsToStrings_string_output() -> None:
    assert convertArgsToStrings(3,4,5,6) == "3_4_5_6"

def test_nameFile_single_item() -> None:
    assert convertArgsToStrings(3) == "3"

def test_convertArgsToStrings_empty_item() -> None:
    assert convertArgsToStrings() == "untitled.hbjson"

def test_convertArgsToStrings_string_input() -> None:
    assert convertArgsToStrings("hello") == "hello"

# convertKeyValueToString
def test_convertKeyValueToString_string_output() -> None:
    # sample dict
    sampleDict = {"a":5, "b":19.0, "c":299}
    assert convertKeyValueToString(sampleDict, key="a") == "a5"
    assert convertKeyValueToString(sampleDict, key="b") == "b19.0"
    assert convertKeyValueToString(sampleDict, key="c") == "c299"

# convertKeyValueToString
def test_convertKeyValueToString_single_item() -> None:
    # sample dict
    sampleDict = {"a":59}
    assert convertKeyValueToString(sampleDict, key="a") == "a59"

