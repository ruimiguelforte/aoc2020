from problems.common import get_input_of_day
import re
from functools import reduce


def is_only_strings(values):
    return all([not x.isnumeric() for y in values for x in y])


def build_rule_map(rules):
    rule_map = {}
    for rule in rules:
        split1 = rule.split(':')
        key = split1[0]
        values = []
        options = split1[1].strip().split('|')
        for option in options:
            value = []
            numbers = option.split(' ')
            for number in numbers:
                if number.strip() != '':
                    entry = number.strip().replace('"', '')
                    value.append(entry)
            if len(value) > 0:
                values.append(value)
        rule_map[key] = values
    for key, values in rule_map.items():
        if is_only_strings(values):
            rule_map[key] = [x for y in values for x in y]
    return rule_map


def ready_to_replace(values, rule_map):
    if type(values[0]) is not list:
        return False
    return all([type(rule_map[x][0]) is not list for y in values for x in y])


def collapse(values):
    return reduce(lambda x, y: [a + b for a in x for b in y], values)


def replace_values(key, rule_map):
    values = rule_map[key]
    new_values = [[rule_map[value] for value in option] for option in values]
    collapsed_values = [x for values in new_values for x in collapse(values)]
    rule_map[key] = collapsed_values
    return rule_map


def unravel_rule_map(rule_map):
    found = False
    for key, values in rule_map.items():
        if ready_to_replace(values, rule_map):
            found = True
            break
    while found:
        rule_map = replace_values(key, rule_map)
        found = False
        for key, values in rule_map.items():
            if ready_to_replace(values, rule_map):
                found = True
                break
    return rule_map


def process_input(input_list):
    rule_pattern = re.compile('[0-9]+: .*')
    rules = []
    strings = []
    for line in input_list:
        clean = line.strip()
        if clean != '':
            if re.match(rule_pattern, clean):
                rules.append(clean)
            else:
                strings.append(clean)
    return strings, rules


def matches_new_rule_zero(x, strings42, strings31):
    test = x
    do31 = True
    times31 = 0
    while do31:
        do31 = False
        for end31 in strings31:
            if test.endswith(end31):
                test = test[:-len(end31)]
                times31 += 1
                do31 = True
    do42 = True
    times42 = 0
    while do42:
        do42 = False
        for start42 in strings42:
            if test.endswith(start42):
                test = test[:-len(start42)]
                times42 += 1
                do42 = True
    return (times31 > 0) and (times42 > times31) and (test == '')


def solve_part1(input_list):
    strings, rules = process_input(input_list)
    rule_map = build_rule_map(rules)
    unravelled_map = unravel_rule_map(rule_map)
    zero_set = set(unravelled_map['0'])
    return sum([1 for x in strings if x in zero_set])


def solve_part2(input_list):
    strings, rules = process_input(input_list)
    rule_map = build_rule_map(rules)
    unravelled_map = unravel_rule_map(rule_map)
    return sum([1 for x in strings if matches_new_rule_zero(x, unravelled_map['42'], unravelled_map['31'])])


if __name__ != 'main':
    print(solve_part1(get_input_of_day(19)))
    print(solve_part2(get_input_of_day(19)))
