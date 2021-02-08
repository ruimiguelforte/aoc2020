from tests.common import get_input_of_day
from problems.day6 import solve_part1, solve_part2


def test_day6_part1():
    test_input = get_input_of_day(6)
    assert solve_part1(test_input) == 11


def test_day6_part2():
    test_input = get_input_of_day(6)
    assert solve_part2(test_input) == 6
