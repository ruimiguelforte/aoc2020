from tests.common import get_input_of_day
from problems.day1 import solve_part1, solve_part2


def test_day1_part1():
    test_input = get_input_of_day(1)
    assert solve_part1(test_input) == 514579


def test_day1_part2():
    test_input = get_input_of_day(1)
    assert solve_part2(test_input) == 241861950
