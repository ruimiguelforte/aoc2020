from tests.common import get_input_of_day
from problems.day19 import solve_part1, solve_part2


def test_day19_part1():
    test_input = get_input_of_day(19)
    assert solve_part1(test_input) == 3


def test_day19_part2():
    test_input = get_input_of_day(19)
    assert solve_part2(test_input) == 12
