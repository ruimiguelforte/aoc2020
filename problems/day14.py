from problems.common import get_input_of_day
import re


def process_input(input_list):
    mem_regex = re.compile(r'mem\[([0-9]+)\]\s+=\s+([0-9]+)')
    instructions = []
    for line in input_list:
        clean = line.strip()
        if clean == '':
            continue
        if clean.startswith('mask'):
            instructions.append(clean.split('=')[1].strip())
        else:
            instructions.append(*re.findall(mem_regex, clean))
    return instructions


def apply_mask36_to(mask36, number):
    number_in_binary = '{:036b}'.format(number)
    for i in range(36):
        if mask36[i] != 'X':
            number_in_binary = number_in_binary[0:i] + mask36[i] + number_in_binary[i+1:]
    return int(number_in_binary, 2)


def get_all_possible_addresses(number_in_binary):
    addresses = ['']
    for letter in number_in_binary:
        if letter != 'X':
            addresses = [address + letter for address in addresses]
        else:
            addresses = [address + '0' for address in addresses] + [address + '1' for address in addresses]
    return list(map(lambda x: int(x,2), addresses))


def get_all_possible_addresses_with_mask(mask36, number):
    number_in_binary = '{:036b}'.format(number)
    for i in range(36):
        if mask36[i] != '0':
            number_in_binary = number_in_binary[0:i] + mask36[i] + number_in_binary[i+1:]
    return get_all_possible_addresses(number_in_binary)


def solve_part1(input_list):
    instructions = process_input(input_list)
    dock_dict = {}
    mask36 = 'X' * 36
    for instruction in instructions:
        if isinstance(instruction, str):
            mask36 = instruction
        else:
            dock_dict[instruction[0]] = apply_mask36_to(mask36, int(instruction[1]))
    return sum(dock_dict.values())


def solve_part2(input_list):
    instructions = process_input(input_list)
    dock_dict = {}
    mask36 = 'X' * 36
    for instruction in instructions:
        if isinstance(instruction, str):
            mask36 = instruction
        else:
            addresses = get_all_possible_addresses_with_mask(mask36, int(instruction[0]))
            for address in addresses:
                dock_dict[address] = int(instruction[1])
    return sum(dock_dict.values())


if __name__ != 'main':
    print(solve_part1(get_input_of_day(14)))
    print(solve_part2(get_input_of_day(14)))
