from problems.common import get_input_of_day
from functools import reduce


def count_trees(slope, pattern_size, right, down):
    trees = 0
    pos = 0
    level_no = 0
    while level_no < len(slope):
        level = slope[level_no]
        if (pos % pattern_size) in level:
            trees += 1
        level_no += down
        pos += right
    return trees


def process_input(input_list):
    slope = []
    for line in input_list:
        x = [i for i, v in enumerate(list(line)) if v == '#']
        slope.append(x)
    pattern_size = len(line.strip())
    return slope, pattern_size


def solve_part1(input_list):
    slope, pattern_size = process_input(input_list)
    return count_trees(slope, pattern_size, 3, 1)


def solve_part2(input_list):
    slope, pattern_size = process_input(input_list)
    forest = [count_trees(slope, pattern_size, right, down) for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
    return reduce((lambda x, y: x * y), forest)


if __name__ != 'main':
    print(solve_part1(get_input_of_day(3)))
    print(solve_part2(get_input_of_day(3)))
