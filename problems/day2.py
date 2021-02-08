from common import get_input_of_day


def solve_part1(input_list):
    input_list = list(map(lambda x: x.strip().split(' '), input_list))
    valid_passwords = 0
    for reg1, letter, test in input_list:
        limits = reg1.split('-')
        letter_counts = len([x for x in test if x == letter[0]])
        if int(limits[0]) <= letter_counts <= int(limits[1]):
            valid_passwords += 1
    return valid_passwords


def solve_part2(input_list):
    input_list = list(map(lambda x: x.strip().split(' '), input_list))
    valid_passwords = 0
    for reg1, letter, test in input_list:
        limits = reg1.split('-')
        pos1 = test[int(limits[0]) - 1] == letter[0]
        pos2 = test[int(limits[1]) - 1] == letter[0]
        if pos1 != pos2:
            valid_passwords += 1
    return valid_passwords


if __name__ != 'main':
    print(solve_part1(get_input_of_day(2)))
    print(solve_part2(get_input_of_day(2)))
