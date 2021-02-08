from problems.common import get_input_of_day
import re


def process_bag_rules(input_list):
    rules = []
    for line in input_list:
        clean = line.strip()
        if clean != '':
            rules.append(clean)
    return rules


def build_parent_dict(rules):
    rule_regex = re.compile(r'((?:[a-z]+)(?: [a-z]+)*)(?= bag)')
    parent_dict = {}
    for rule in rules:
        matches = rule_regex.findall(rule)
        parent_colour = matches[0]
        for colour in matches[1:]:
            if colour != parent_colour:
                parent_dict.setdefault(colour, set()).add(parent_colour)
    return parent_dict


def build_container_dict(rules):
    daddy_regex = re.compile(r'((?:[a-z]+)(?: [a-z]+)*)(?= bags contain)')
    child_regex = re.compile(r'([0-9]+) ((?:[a-z]+)(?: [a-z]+)*)(?= bag)')
    container_dict = {}
    for rule in rules:
        big_bag = daddy_regex.match(rule).group(0)
        inside_bags = child_regex.findall(rule)
        for qty, colour in inside_bags:
            container_dict.setdefault(big_bag, []).append((int(qty), colour))
    return container_dict


def bags_inside(colour, container_dict):
    total_qty = 0
    if colour in container_dict:
        for qty, inside_colour in container_dict[colour]:
            total_qty += qty * (1 + bags_inside(inside_colour, container_dict))
    return total_qty


def solve_part1(input_list):
    rules = process_bag_rules(input_list)
    parent_dict = build_parent_dict(rules)
    allowable_colours = set()
    to_search = {'shiny gold'}
    while len(to_search) > 0:
        current_colour = to_search.pop()
        if current_colour in parent_dict:
            parents = parent_dict[current_colour]
            for parent in parents:
                if parent not in allowable_colours:
                    allowable_colours.add(parent)
                    to_search.add(parent)
    return len(allowable_colours)


def solve_part2(input_list):
    rules = process_bag_rules(input_list)
    container_dict = build_container_dict(rules)
    return bags_inside('shiny gold', container_dict)


if __name__ != 'main':
    print(solve_part1(get_input_of_day(7)))
    print(solve_part2(get_input_of_day(7)))
