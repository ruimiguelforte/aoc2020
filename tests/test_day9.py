from tests.common import get_input_of_day
from problems.day9 import solve_part1, solve_part2


def test_day9_part1():
    test_input = get_input_of_day(9)
    preamble = 5
    assert solve_part1(test_input, preamble) == 127


def test_day9_part2():
    test_input = get_input_of_day(9)
    preamble = 5
    assert solve_part2(test_input, preamble) == 62
