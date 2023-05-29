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


@pytest.mark.leetcode
@pytest.mark.hard
@pytest.mark.parametrize("l1, l2, result", [
    ([1, 2], [3, 4], 2.5),
    ([5, 11, 26, 41], [0, 13], 12),
    ([1], [2], 1.5),
    ([44, 55, 56, 90, 91, 93, 1005, 1006, 1332, 1543], [5, 23, 31, 1100, 1900], 91),
])
def test_find_median_sorted_arrays(l1, l2, result, solution):
    assert solution.findMedianSortedArrays(l1, l2) == result
