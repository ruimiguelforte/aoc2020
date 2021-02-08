from problems.common import get_input_of_day
from functools import reduce


def process_input(input_list):
    rules = {}
    your_ticket = []
    nearby_tickets = []
    section = 'rules'
    for line in input_list:
        if 'your ticket' in line:
            section = 'your_ticket'
        elif 'nearby tickets' in line:
            section = 'nearby_tickets'
        else:
            clean = line.strip()
            if clean == '':
                continue
            if section == 'rules':
                key, value = get_rule(clean)
                rules[key] = value
            elif section == 'your_ticket':
                your_ticket = get_ticket(clean)
            else:
                current_ticket = get_ticket(clean)
                nearby_tickets.append(current_ticket)
    return rules, your_ticket, nearby_tickets


def get_rule(my_str):
    first_split = my_str.split(':')
    second_split = first_split[1].strip().split(' or ')
    first_range = second_split[0].split('-')
    second_range = second_split[1].split('-')
    return (first_split[0]), ((int(first_range[0]), int(first_range[1])), (int(second_range[0]), int(second_range[1])))


def get_ticket(ticket_line):
    return list(map(int, ticket_line.strip().split(',')))


def matches_rule(ranges, my_number):
    first_min = ranges[0][0]
    first_max = ranges[0][1]
    second_min = ranges[1][0]
    second_max = ranges[1][1]
    return (first_min <= my_number <= first_max) or (second_min <= my_number <= second_max)


def matches_any_rule(rules, my_number):
    for rule in rules.values():
        if matches_rule(rule, my_number):
            return True
    return False


def all_match_rule(ranges, my_number_list):
    return all([matches_rule(ranges, x) for x in my_number_list])


def get_matching_rules(rules, my_number_list):
    return [key for key in rules.keys() if all_match_rule(rules[key], my_number_list)]


def solve_part1(input_list):
    rules, your_ticket, nearby_tickets = process_input(input_list)
    invalid_numbers = [number for ticket in nearby_tickets for number in ticket if not matches_any_rule(rules, number)]
    return sum(invalid_numbers)


def solve_part2(input_list):
    rules, your_ticket, nearby_tickets = process_input(input_list)
    valid_tickets = [ticket for ticket in nearby_tickets if all(list(map(lambda x: matches_any_rule(rules, x), ticket)))]
    possible_assignments = [get_matching_rules(rules, [ticket[i] for ticket in valid_tickets]) for i in
                            range(len(nearby_tickets[0]))]
    leftover_assignments = possible_assignments.copy()
    assignment_dict = {}
    while len(assignment_dict) < len(rules):
        for i in range(len(leftover_assignments)):
            if len(leftover_assignments[i]) == 1:
                key = leftover_assignments[i][0]
                assignment_dict[i] = key
                leftover_assignments = [[x for x in sublist if x != key] for sublist in leftover_assignments]
    assignment_dict = {value: key for key, value in assignment_dict.items()}
    return reduce(lambda x, y: x * y,
           [your_ticket[assignment_dict[key]] for key in assignment_dict.keys() if key.startswith('departure')])


if __name__ != 'main':
    print(solve_part1(get_input_of_day(16)))
    print(solve_part2(get_input_of_day(16)))
