from problems.common import get_input_of_day
from functools import reduce


def process_group_sets(input_list):
    group_sets = []
    current_group = []
    for line in input_list:
        clean = line.strip()
        if clean == '':
            group_sets.append(current_group)
            current_group = []
        else:
            current_group.append(set(clean))
    if len(current_group) != 0:
        group_sets.append(current_group)
    return group_sets


def solve_part1(input_list):
    group_sets = process_group_sets(input_list)
    union_sets = [set.union(*group) for group in group_sets]
    return reduce(lambda x,y: x + y, [len(x) for x in union_sets])


def solve_part2(input_list):
    group_sets = process_group_sets(input_list)
    intersection_sets = [set.intersection(*group) for group in group_sets]
    return reduce(lambda x,y: x + y, [len(x) for x in intersection_sets])


if __name__ != 'main':
    print(solve_part1(get_input_of_day(6)))
    print(solve_part2(get_input_of_day(6)))
