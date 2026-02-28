import pytest
from lib.palindrome import longest_palindromic_substring


# 
# Basic Valid Cases


def test_odd_length_palindrome():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]


def test_even_length_palindrome():
    assert longest_palindromic_substring("cbbd") == "bb"


def test_full_string_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


# -------------------------
# Edge Cases


def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_two_different_characters():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_no_repeating_characters():
    result = longest_palindromic_substring("abcdef")
    assert len(result) == 1


def test_long_string():
    s = "a" * 1000
    assert longest_palindromic_substring(s) == s


#############################

def test_non_string_input():
    with pytest.raises(TypeError):
        longest_palindromic_substring(123)
