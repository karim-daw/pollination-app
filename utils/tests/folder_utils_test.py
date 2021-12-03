""" example of test module in pytest"""

from folder_utils import total
from folder_utils import nameFile

# total
def test_total_empty() -> None:
    """ Total of empty list should be 0.0"""
    assert total([]) == 0.0

def test_total_single_item() -> None:
    assert total([110.0]) == 110.0

def test_total_many_item() -> None:
    assert total([110.0,2.0,3.0]) == 115.0

# nameFile
def test_nameFile_string_output() -> None:
    assert nameFile(3,4,5,6) == "3_4_5_6"

def test_nameFile_single_item() -> None:
    assert nameFile(3) == "3"

def test_nameFile_empty_item() -> None:
    assert nameFile() == "untitled.hbjson"

def test_nameFile_string_input() -> None:
    assert nameFile("hello") == "hello"