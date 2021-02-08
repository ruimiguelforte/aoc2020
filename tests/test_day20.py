from tests.common import get_input_of_day
from problems.day20 import solve_part1, solve_part2


def test_day20_part1():
    test_input = get_input_of_day(20)
    assert solve_part1(test_input) == 20899048083289


def test_day20_part2():
    test_input = get_input_of_day(20)
    assert solve_part2(test_input) == 273
