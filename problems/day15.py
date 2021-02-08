def initialize_problem(number_list):
    return ({number_list[i]: [i + 1] for i in range(len(number_list))}), number_list[-1], len(number_list) + 1


def get_next_number(number_map, most_recent_number, turn):
    past_occurrences = number_map[most_recent_number]
    if len(past_occurrences) == 1:
        spoken = 0
    else:
        spoken = past_occurrences[-1] - past_occurrences[-2]
    number_map[spoken] = number_map.get(spoken, [])[-1:] + [turn]
    return number_map, spoken, turn + 1


def get_sequence_at(number_list, max_turn):
    number_map, spoken, turn = initialize_problem(number_list)
    while turn <= max_turn:
        number_map, spoken, turn = get_next_number(number_map, spoken, turn)
    return spoken


def solve_part1(input_list):
    return get_sequence_at(input_list, 2020)


def solve_part2(input_list):
    return get_sequence_at(input_list, 30000000)


if __name__ != 'main':
    print(solve_part1([20, 0, 1, 11, 6, 3]))
    print(solve_part2([20, 0, 1, 11, 6, 3]))