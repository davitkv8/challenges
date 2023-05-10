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
