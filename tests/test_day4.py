from tests.common import get_input_of_day
from problems.day4 import solve_part1, solve_part2


def test_day4_part1():
    test_input = get_input_of_day(4)
    assert solve_part1(test_input) == 2


def test_day4_part2():
    test_input = get_input_of_day(4)
    assert solve_part2(test_input) == 2
