def perform_move(cups, current_cup_index):
    new_cups = cups[current_cup_index:] + cups[0:current_cup_index]
    current_cup = new_cups[0]
    next_three = new_cups[1:4]
    destination_cup = int(current_cup) - 1
    while str(destination_cup) in list(next_three) or (destination_cup < 1):
        destination_cup -= 1
        if destination_cup <= 0:
            destination_cup = len(new_cups)
    destination_cup = str(destination_cup)
    new_cups = new_cups[0] + new_cups[4:]
    destination_index = new_cups.find(destination_cup)
    new_cups = new_cups[0:destination_index + 1] + next_three + new_cups[destination_index + 1:]
    new_index = new_cups.find(current_cup) + 1
    if new_index >= len(new_cups):
        new_index = 0
    return new_cups, new_index


def perform_n_moves(cups, current_cup_index, n):
    for _ in range(n):
        cups, current_cup_index = perform_move(cups, current_cup_index)
    index_1 = cups.find('1')
    new_cups = cups[index_1:] + cups[0:index_1]
    return new_cups[1:]


def make_circular_map(mylist):
    cmap = {}
    first = None
    current = None
    for element in mylist:
        if first is None:
            first = element
        else:
            cmap[current] = element
        current = element
    cmap[current] = first
    return cmap


def perform_map_move(cups_map, current_cup):
    next_one = cups_map[current_cup]
    next_two = cups_map[next_one]
    next_three = cups_map[next_two]
    next_cup = cups_map[next_three]
    destination_cup = current_cup - 1
    while (destination_cup in {next_one, next_two, next_three}) or (destination_cup < 1):
        destination_cup -= 1
        if destination_cup <= 0:
            destination_cup = len(cups_map.keys())
    cups_map[current_cup] = next_cup
    cups_map[next_three] = cups_map[destination_cup]
    cups_map[destination_cup] = next_one
    return cups_map, next_cup


def perform_n_map_moves(cups_map, current_cup, n):
    for i in range(n):
        cups_map, current_cup = perform_map_move(cups_map, current_cup)
    return cups_map, current_cup


def solve_part1(cups):
    current_cup_index = 0
    return perform_n_moves(cups, current_cup_index, 100)


def solve_part2(cups):
    puzzle_list = list(cups)
    temp = list(range(1, 10000001))
    cups2 = [int(puzzle_list[i]) if i < len(puzzle_list) else temp[i] for i in range(1000000)]
    del temp
    cups_map = make_circular_map(cups2)
    cups_map, current_cup = perform_n_map_moves(cups_map, 3, 10000000)
    return cups_map[1] * cups_map[cups_map[1]]


if __name__ != 'main':
    print(solve_part1('362981754'))
    print(solve_part2('362981754'))
