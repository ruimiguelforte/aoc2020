from problems.common import get_input_of_day
import re


def get_passports(input_list):
    valid_field = re.compile(r'([a-z][^:\s]*)\:([^\s]+)')
    passports = []
    current = {}
    for line in input_list:
        if line.strip() == '':
            passports.append(current)
            current = {}
        else:
            for (key, value) in re.findall(valid_field, line):
                current[key] = value
    # If you have no empty line at the end of the document
    if current != {}:
        passports.append(current)
    return passports


def solve_part1(input_list):
    passports = get_passports(input_list)
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid_passports = 0
    for passport in passports:
        if required_keys.issubset(passport.keys()):
            valid_passports += 1
    return valid_passports


def solve_part2(input_list):
    passports = get_passports(input_list)
    validation_dict = {'byr': re.compile(r'19[2-9][0-9]|200[0-2]'),
                       'iyr': re.compile(r'20(1[0-9]|20)'),
                       'eyr': re.compile(r'20(2[0-9]|30)'),
                       'hgt': re.compile(r'1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in'),
                       'hcl': re.compile(r'#[0-9a-f]{6}'),
                       'ecl': re.compile('amb|blu|brn|gry|grn|hzl|oth'),
                       'pid': re.compile('[0-9]{9}')}
    valid_passports = 0
    for passport in passports:
        valid = True
        for vkey, vvalue in validation_dict.items():
            if vkey not in passport or not re.fullmatch(vvalue, passport[vkey]):
                valid = False
        if valid:
            valid_passports += 1
    return valid_passports


if __name__ != 'main':
    print(solve_part1(get_input_of_day(4)))
    print(solve_part2(get_input_of_day(4)))
