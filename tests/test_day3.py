from tests.common import get_input_of_day
from problems.day3 import solve_part1, solve_part2


def test_day3_part1():
    test_input = get_input_of_day(3)
    assert solve_part1(test_input) == 7


def test_day3_part2():
    test_input = get_input_of_day(3)
    assert solve_part2(test_input) == 336
