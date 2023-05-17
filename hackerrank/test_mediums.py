import pytest

from mediums import *
from long_inputs import *


@pytest.mark.medium
@pytest.mark.parametrize('year, output', [
    (1800, False),
    (1990, False),
    (2100, False),
    (2200, False),
    (2300, False),
    (2500, False),
    (2000, True),
    (2400, True),
    (2023, False),
])
def test_is_leap(year: int, output: bool):
    assert is_leap(year) == output


@pytest.mark.medium
@pytest.mark.parametrize('string, result', [
    ('BANANA', 'Stuart 12'),
    ('BAANANAS', 'Kevin 19'),
    ('ANANAS', 'Kevin 12'),
    ('BANANANAAAS', 'Draw'),
    (MINION_GAME_LONG_INPUT_1, 'Stuart 7501500')
])
def test_minion_game(string: int, result: bool):
    assert minion_game(string) == result


@pytest.mark.medium
@pytest.mark.parametrize("string, split_size, result", [
    ("AABCAAADA", 3, "AB\nCA\nAD\n"),
    ("AAABCADDE", 3, "A\nBCA\nDE\n"),
    (MERGE_THE_TOOLS_LONG_INPUT_1, 5424, "BWMNAKIJHOZXVGQYPLCEUDSFTR\n"),
])
def test_merge_the_tools(string, split_size, result, capsys):
    merge_the_tools(string, split_size)
    captured = capsys.readouterr()
    assert captured.out == result


@pytest.mark.math
@pytest.mark.medium
@pytest.mark.parametrize("ab, bc, result", [
    (10, 10, "45°"),
    (6, 8, "37°"),
    (101, 1, "89°"),
    (56, 54, "46°"),
])
def test_find_angle(ab, bc, result, capsys):
    find_angle(ab, bc)
    captured = capsys.readouterr()
    assert captured.out.replace("\n", "") == result


@pytest.mark.medium
@pytest.mark.parametrize("t1, t2, result", [
    ("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000", 25200),
    ("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000", 88200)
])
def test_time_delta(t1, t2, result):
    assert time_delta(t1, t2) == result
