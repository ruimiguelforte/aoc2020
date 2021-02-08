from tests.common import get_input_of_day
from problems.day22 import solve_part1, solve_part2


def test_day22_part1():
    test_input = get_input_of_day(22)
    assert solve_part1(test_input) == 306


def test_day22_part2():
    test_input = get_input_of_day(22)
    assert solve_part2(test_input) == 291
