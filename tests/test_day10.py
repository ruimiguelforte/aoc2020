from tests.common import get_input_of_day
from problems.day10 import solve_part1, solve_part2


def test_day10_part1():
    test_input = get_input_of_day(10)
    assert solve_part1(test_input) == 220


def test_day10_part2():
    test_input = get_input_of_day(10)
    assert solve_part2(test_input) == 19208
