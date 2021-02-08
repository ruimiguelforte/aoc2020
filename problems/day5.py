from problems.common import get_input_of_day
import re


def get_seat_id(seat_str):
    row = seat_str[0:7]
    row = re.sub('F', '0', row)
    row = re.sub('B', '1', row)
    row_num = int(row, 2)
    col = seat_str[7:]
    col = re.sub('L', '0', col)
    col = re.sub('R', '1', col)
    col_num = int(col, 2)
    return row_num * 8 + col_num


def solve_part1(input_list):
    seat_ids = list(map(lambda x: get_seat_id(x.strip()), input_list))
    max_id = 0
    for current_ID in seat_ids:
        if current_ID > max_id:
            max_id = current_ID
    return max_id


def solve_part2(input_list):
    seat_ids = list(map(lambda x: get_seat_id(x.strip()), input_list))
    sorted_ids = sorted(seat_ids)
    expected_id = sorted_ids[0]
    for current_id in sorted_ids:
        if expected_id != current_id:
            break
        expected_id += 1
    return expected_id


if __name__ != 'main':
    print(solve_part1(get_input_of_day(5)))
    print(solve_part2(get_input_of_day(5)))
