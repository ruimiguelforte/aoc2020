from tests.common import get_input_of_day
from problems.day13 import solve_part1, solve_part2


def test_day13_part1():
    test_input = get_input_of_day(13)
    assert solve_part1(test_input) == 295


def test_day13_part2():
    test_input = get_input_of_day(13)
    assert solve_part2(test_input) == 1068781
