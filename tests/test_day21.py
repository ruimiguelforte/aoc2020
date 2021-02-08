from tests.common import get_input_of_day
from problems.day21 import solve_part1, solve_part2


def test_day21_part1():
    test_input = get_input_of_day(21)
    assert solve_part1(test_input) == 5


def test_day21_part2():
    test_input = get_input_of_day(21)
    assert solve_part2(test_input) == 'mxmxvkd,sqjhc,fvjkl'
