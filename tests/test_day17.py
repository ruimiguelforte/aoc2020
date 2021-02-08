from tests.common import get_input_of_day
from problems.day17 import solve_part1, solve_part2


def test_day17_part1():
    test_input = get_input_of_day(17)
    assert solve_part1(test_input) == 112


def test_day17_part2():
    test_input = get_input_of_day(17)
    assert solve_part2(test_input) == 848
