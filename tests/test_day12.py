from tests.common import get_input_of_day
from problems.day12 import solve_part1, solve_part2


def test_day12_part1():
    test_input = get_input_of_day(12)
    assert solve_part1(test_input) == 25


def test_day12_part2():
    test_input = get_input_of_day(12)
    assert solve_part2(test_input) == 286
