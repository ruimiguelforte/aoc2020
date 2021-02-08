from tests.common import get_input_of_day
from problems.day11 import solve_part1, solve_part2


def test_day11_part1():
    test_input = get_input_of_day(11)
    assert solve_part1(test_input) == 37


def test_day11_part2():
    test_input = get_input_of_day(11)
    assert solve_part2(test_input) == 26
