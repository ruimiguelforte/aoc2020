from tests.common import get_input_of_day
from problems.day18 import solve_part1, solve_part2


def test_day18_part1():
    test_input = get_input_of_day(18)
    assert solve_part1(test_input) == 51 + 26 + 437 + 12240 + 13632


def test_day18_part2():
    test_input = get_input_of_day(18)
    assert solve_part2(test_input) == 51 + 46 + 1445 + 669060 + 23340
