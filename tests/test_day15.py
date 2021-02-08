from problems.day15 import solve_part1, solve_part2


def test_day15_part1():
    test_input = [0, 3, 6]
    assert solve_part1(test_input) == 436


def test_day15_part2():
    test_input = [0, 3, 6]
    assert solve_part2(test_input) == 175594
