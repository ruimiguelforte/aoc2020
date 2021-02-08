from tests.common import get_input_of_day
from problems.day7 import solve_part1, solve_part2


def test_day7_part1():
    test_input = get_input_of_day(7)
    assert solve_part1(test_input) == 4


def test_day7_part2():
    test_input = get_input_of_day(7)
    assert solve_part2(test_input) == 32
