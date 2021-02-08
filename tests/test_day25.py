from tests.common import get_input_of_day
from problems.day25 import solve_part1


def test_day25_part1():
    test_input = get_input_of_day(25)
    assert solve_part1(test_input) == 14897079

