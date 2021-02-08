from tests.common import get_input_of_day
from problems.day16 import solve_part1


def test_day16_part1():
    test_input = get_input_of_day(16)
    assert solve_part1(test_input) == 71
