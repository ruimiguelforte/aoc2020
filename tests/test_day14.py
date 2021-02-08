from tests.common import get_input_of_day
from problems.day14 import solve_part1, solve_part2


def test_day14_part1():
    test_input = get_input_of_day(14)
    assert solve_part1(test_input) == 165


def test_day14_part2():
    test_input = ['mask = 000000000000000000000000000000X1001X', 'mem[42] = 100',
                  'mask = 00000000000000000000000000000000X0XX', 'mem[26] = 1']
    assert solve_part2(test_input) == 208
