from problems.common import get_input_of_day


def transform_subject_number(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = value * subject_number
        value = value % 20201227
    return value


def find_loop_size(subject_number, pk):
    loop_size = 1
    value = 1
    while loop_size < 10000000:
        value = value * subject_number
        value = value % 20201227
        if value == pk:
            return loop_size
        loop_size += 1
    return -1


def process_input(input_list):
    card_pk = int(input_list[0])
    door_pk = int(input_list[1])
    return card_pk, door_pk


def solve_part1(input_list):
    card_pk, door_pk = process_input(input_list)
    card_loop_size = find_loop_size(7, card_pk)
    door_loop_size = find_loop_size(7, door_pk)
    encryyption_key_from_card = transform_subject_number(door_pk, card_loop_size)
    encryyption_key_from_door = transform_subject_number(card_pk, door_loop_size)
    assert encryyption_key_from_card == encryyption_key_from_door
    return encryyption_key_from_card


if __name__ != 'main':
    print(solve_part1(get_input_of_day(25)))
