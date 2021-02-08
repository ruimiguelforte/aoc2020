from tests.common import get_input_of_day
from problems.day2 import solve_part1, solve_part2


def test_day2_part1():
    test_input = get_input_of_day(2)
    assert solve_part1(test_input) == 2


def test_day2_part2():
    test_input = get_input_of_day(2)
    assert solve_part2(test_input) == 1
