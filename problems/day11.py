from problems.common import get_input_of_day


def process_board(input_list):
    board = []
    for line in input_list:
        clean = line.strip()
        if clean != '':
            board.append(list(clean))
    return board


def count_adjacent_occupied_seats(board, row, column):
    seats = 0
    for test_row in (row - 1, row, row + 1):
        for test_column in (column - 1, column, column + 1):
            if not(test_column == column and test_row == row) and 0 <= test_column < len(board[0]) and \
                    0 <= test_row < len(board) and board[test_row][test_column] == '#':
                seats += 1
    return seats


def create_next_board_state(board):
    new_board = []
    for row in range(len(board)):
        new_row = []
        for column in range(len(board[0])):
            current_seat_state = board[row][column]
            if current_seat_state == '.':
                new_row.append('.')
            else:
                occupied_seats = count_adjacent_occupied_seats(board, row, column)
                if current_seat_state == 'L':
                    new_state = '#' if occupied_seats == 0 else 'L'
                else:
                    new_state = 'L' if occupied_seats >= 4 else '#'
                new_row.append(new_state)
        new_board.append(new_row)
    return new_board


def progress_till_conversion(board):
    current_board = board
    new_board = create_next_board_state(board)
    while new_board != current_board:
        current_board = new_board
        new_board = create_next_board_state(current_board)
    return current_board


def count_visible_occupied_seats(board, row, column, verbose=False):
    max_no = max(len(board), len(board[0]))
    # Process 8 directions
    rows_to_check = [[board[row][x] for x in range(column - 1, -1, -1) if x >= 0 and board[row][x] != '.'],
                     [board[row][x] for x in range(column + 1, len(board[row])) if
                      x < len(board[row]) and board[row][x] != '.'],
                     [board[x][column] for x in range(row - 1, -1, -1) if x >= 0 and board[x][column] != '.'],
                     [board[x][column] for x in range(row + 1, len(board)) if
                      x < len(board) and board[x][column] != '.'],
                     [board[row - x][column - x] for x in range(1, max_no) if (row - x) >= 0 and (column - x) >= 0
                      and board[row - x][column - x] != '.'], [board[row + x][column + x] for x in range(1, max_no) if
                                                               (row + x) < len(board) and (column + x) < len(board[row])
                                                               and board[row + x][column + x] != '.'],
                     [board[row - x][column + x] for x in range(1, max_no) if
                      (row - x) >= 0 and (column + x) < len(board[row])
                      and board[row - x][column + x] != '.'], [board[row + x][column - x] for x in range(1, max_no) if
                                                               (row + x) < len(board) and (column - x) >= 0
                                                               and board[row + x][column - x] != '.']]
    if verbose:
        print(rows_to_check)
    return sum([1 for row in rows_to_check if row != [] and row[0] == '#'])


def create_next_fancy_board_state(board):
    new_board = []
    for row in range(len(board)):
        new_row = []
        for column in range(len(board[0])):
            current_seat_state = board[row][column]
            if current_seat_state == '.':
                new_row.append('.')
            else:
                occupied_seats = count_visible_occupied_seats(board, row, column)
                if current_seat_state == 'L':
                    new_state = '#' if occupied_seats == 0 else 'L'
                else:
                    new_state = 'L' if occupied_seats >= 5 else '#'
                new_row.append(new_state)
        new_board.append(new_row)
    return new_board


def progress_till_fancy_conversion(board, verbose=False):
    current_board = board
    new_board = create_next_fancy_board_state(board)
    while new_board != current_board:
        current_board = new_board
        new_board = create_next_fancy_board_state(current_board)
        if verbose:
            print(new_board)
    return current_board


def solve_part1(input_list):
    board = process_board(input_list)
    final_board = progress_till_conversion(board)
    final_occupied = [1 for row in final_board for element in row if element == '#']
    return sum(final_occupied)


def solve_part2(input_list):
    board = process_board(input_list)
    final_fancy_board = progress_till_fancy_conversion(board)
    final_fancy_occupied = [1 for row in final_fancy_board for element in row if element == '#']
    return sum(final_fancy_occupied)


if __name__ != 'main':
    print(solve_part1(get_input_of_day(11)))
    print(solve_part2(get_input_of_day(11)))
