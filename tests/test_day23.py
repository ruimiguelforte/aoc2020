from problems.day23 import solve_part1, solve_part2


def test_day23_part1():
    test_input = '389125467'
    assert solve_part1(test_input) == '67384529'


def test_day23_part2():
    test_input = '389125467'
    assert solve_part2(test_input) == 149245887792
