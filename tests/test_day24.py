from tests.common import get_input_of_day
from problems.day24 import solve_part1, solve_part2


def test_day24_part1():
    test_input = get_input_of_day(24)
    assert solve_part1(test_input) == 10


def test_day24_part2():
    test_input = get_input_of_day(24)
    assert solve_part2(test_input) == 2208
