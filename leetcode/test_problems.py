import pytest

from problems import *


@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.leetcode
@pytest.mark.easy
@pytest.mark.parametrize("string, result", [
    ("XVI", 16),
    ("III", 3),
    ("XIV", 14),
    ("XX", 20),
    ("IV", 4),
])
def test_roman_to_int_with_fixture(string, result, solution):
    assert solution.roman_to_int(string) == result


@pytest.mark.leetcode
@pytest.mark.medium
@pytest.mark.parametrize("string, result", [
    ("akpoikpoiukpoiuyt", 7),
    ("abcdabcee", 5),
    ("polopalace", 4),
    ("xxxxxyyytepoexy", 5),
])
def test_length_of_longest_substring(string, result, solution):
    assert solution.length_of_longest_substring(string) == result


@pytest.mark.leetcode
@pytest.mark.medium
@pytest.mark.parametrize("string, row_num, result", [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("zxvbnmasdf", 2, "zvnadxbmsf"),
    ("!@#%^&*()", 6, "!@#)%(^*&"),
    ("HELLO_WORLD_TEST_CASE", 4, "HWTAE_O_ECSLORDS_ELLT"),
])
def test_zigzag_conversion(string, row_num, result, solution):
    assert solution.zigzag_conversion(string, row_num) == result
