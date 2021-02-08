from problems.common import get_input_of_day


def process_commands(input_list):
    input_commands = []
    for line in input_list:
        clean = line.strip()
        if clean != '':
            bits = clean.split(' ')
            input_commands.append((bits[0], int(bits[1])))
    return input_commands


def execute_program(commands):
    i = 0
    acc = 0
    have_seen = set()
    while i < len(commands):
        if i in have_seen:
            break
        have_seen.add(i)
        command = commands[i]
        if command[0] == 'acc':
            acc += command[1]
        if command[0] == 'jmp':
            i += command[1]
        else:
            i += 1
    terminated = (i == len(commands))
    return terminated, acc, have_seen


def get_new_program(input_commands, pos):
    new_commands = input_commands.copy()
    change_instruction = new_commands[pos][0]
    new_instruction = 'jmp' if change_instruction == 'nop' else 'nop'
    new_commands[pos] = (new_instruction, new_commands[pos][1])
    return new_commands


def solve_part1(input_list):
    input_commands = process_commands(input_list)
    terminated, acc, have_seen = execute_program(input_commands)
    return acc


def solve_part2(input_list):
    input_commands = process_commands(input_list)
    terminated, acc, have_seen = execute_program(input_commands)
    for pos in have_seen:
        instruction = input_commands[pos]
        if instruction == 'acc':
            continue
        new_commands = get_new_program(input_commands, pos)
        terminated, acc, have_seen = execute_program(new_commands)
        if terminated:
            break
    return acc


if __name__ != 'main':
    print(solve_part1(get_input_of_day(8)))
    print(solve_part2(get_input_of_day(8)))
