from problems.common import get_input_of_day
import math
import copy


def rotate_90_clockwise(tile):
    return [[tile[row_index][col_index] for row_index in range(len(tile) - 1, -1, -1)]
            for col_index in range(len(tile))]


def flip_horizontally(tile):
    return [list(reversed(row)) for row in tile]


def print_tile(tile):
    for row in tile:
        print(''.join(row))


def create_orientations(tiles):
    orientations = {}
    for key, tile in tiles.items():
        orientations[key] = {}
        flipped_tile = flip_horizontally(tile)
        for turn in ('0', '90', '180', '270'):
            orientations[key][turn] = tile
            tile = rotate_90_clockwise(tile)
            orientations[key]['f_' + turn] = flipped_tile
            flipped_tile = rotate_90_clockwise(flipped_tile)
    return orientations


def get_top_border(tile):
    return ''.join(tile[0])


def get_bottom_border(tile):
    return ''.join(tile[len(tile) - 1])


def get_left_border(tile):
    return ''.join([row[0] for row in tile])


def get_right_border(tile):
    return ''.join([row[len(row) - 1] for row in tile])


def invert_border_map(tile_map):
    inv_map = {}
    for k1, v1 in tile_map.items():
        for k2, v2 in v1.items():
            inv_map.setdefault(v2, []).append((k1, k2))
    return inv_map


def is_valid_placement(tile, above, below, left, right, top_map, bottom_map, left_map, right_map):
    top_border = get_top_border(tile)
    matches_above = (above == '') or (above in bottom_map[top_border])
    if not matches_above:
        return False
    bottom_border = get_bottom_border(tile)
    matches_below = (below == '') or (below in top_map[bottom_border])
    if not matches_below:
        return False
    left_border = get_left_border(tile)
    matches_left = (left == '') or (left in right_map[left_border])
    if not matches_left:
        return False
    right_border = get_right_border(tile)
    matches_right = (right == '') or (right in left_map[right_border])
    return matches_right


def get_possible_tiles(above, below, left, right, unplaced_tile_keys, orientations, top_map, bottom_map, left_map,
                       right_map):
    possible_tiles = []
    for tile_key in unplaced_tile_keys:
        for orientation_key, orientation in orientations[tile_key].items():
            if is_valid_placement(orientation, above, below, left, right, top_map, bottom_map, left_map, right_map):
                possible_tiles.append((tile_key, orientation_key))
    return sorted(possible_tiles)


def get_next_open_position(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '':
                return i, j
    return -1, -1


def fill_board(board, unplaced_tile_keys, orientations, top_map, bottom_map, left_map, right_map):
    i, j = get_next_open_position(board)
    if (i, j) == (-1, -1):
        return True, board
    above = board[i - 1][j] if i > 0 else ''
    below = board[i + 1][j] if i < (len(board) - 1) else ''
    left = board[i][j - 1] if j > 0 else ''
    right = board[i][j + 1] if j < (len(board) - 1) else ''
    possible_tiles = get_possible_tiles(above, below, left, right, unplaced_tile_keys, orientations, top_map,
                                        bottom_map, left_map, right_map)
    if len(possible_tiles) == 0:
        return False, board
    for tile_key, orientation_key in possible_tiles:
        new_unplaced_tile_keys = unplaced_tile_keys.copy()
        new_unplaced_tile_keys.remove(tile_key)
        new_board = copy.deepcopy(board)
        new_board[i][j] = (tile_key, orientation_key)
        succeeded, new_board = fill_board(new_board, new_unplaced_tile_keys, orientations, top_map, bottom_map,
                                          left_map, right_map)
        if succeeded:
            return True, new_board
    return False, board


def process_input(input_list):
    tile_no = ''
    tiles = {}
    image = []
    for line in input_list:
        clean = line.strip()
        if clean == '':
            tiles[tile_no] = image
            tile_no = ''
            image = []
        elif line.startswith('Tile'):
            tile_no = int(clean.split(' ')[1][:-1])
        else:
            image.append(list(clean))
    if tile_no != '':
        tiles[tile_no] = image
    return tiles


def remove_border(image):
    return [[image[i][j] for j in range(1, len(image) - 1)] for i in range(1, len(image) - 1)]


def matches_search_image(image, search_image):
    for i in range(len(search_image)):
        for j in range(len(search_image[0])):
            if (search_image[i][j] != ' ') and (search_image[i][j] != image[i][j]):
                return False
    return True


def count_monsters(monsters, search_image):
    search_rows = len(search_image)
    search_columns = len(search_image[0])
    tile = copy.deepcopy(monsters)
    flipped_tile = flip_horizontally(tile)
    for turn in ('0', '90', '180', '270'):
        for flipped in (True, False):
            current_tile = flipped_tile if flipped else tile
            num_monsters = 0
            for i in range(len(current_tile) - search_rows):
                for j in range(len(current_tile[0]) - search_columns):
                    window = [current_tile[x][j:j + search_columns] for x in range(i, i + search_rows)]
                    if matches_search_image(window, search_image):
                        num_monsters += 1
            if num_monsters > 0:
                return num_monsters
        tile = rotate_90_clockwise(tile)
        flipped_tile = rotate_90_clockwise(flipped_tile)
    return 0


def prepare_and_fill_board(tiles):
    board_size = int(math.sqrt(len(tiles.keys())))
    orientations = create_orientations(tiles)
    top_map = invert_border_map(
        {k1: {k2: get_top_border(v2) for k2, v2 in v1.items()} for k1, v1 in orientations.items()})
    bottom_map = invert_border_map(
        {k1: {k2: get_bottom_border(v2) for k2, v2 in v1.items()} for k1, v1 in orientations.items()})
    left_map = invert_border_map(
        {k1: {k2: get_left_border(v2) for k2, v2 in v1.items()} for k1, v1 in orientations.items()})
    right_map = invert_border_map(
        {k1: {k2: get_right_border(v2) for k2, v2 in v1.items()} for k1, v1 in orientations.items()})
    board = [['' for _ in range(board_size)] for _ in range(board_size)]
    unplaced_tile_keys = set(orientations.keys())
    succeeded, new_board = fill_board(board, unplaced_tile_keys, orientations, top_map, bottom_map, left_map, right_map)
    return succeeded, new_board, board_size, orientations


def solve_part1(input_list):
    tiles = process_input(input_list)
    succeeded, new_board, board_size, orientations = prepare_and_fill_board(tiles)
    return new_board[0][0][0] * new_board[0][board_size - 1][0] * new_board[board_size - 1][0][0] * \
           new_board[board_size - 1][board_size - 1][0]


def solve_part2(input_list):
    tiles = process_input(input_list)
    succeeded, new_board, board_size, orientations = prepare_and_fill_board(tiles)
    borderless_images = [[remove_border(orientations[tile_key][orientation_key]) for tile_key, orientation_key in row]
                         for row in new_board]
    monsters = [[element for image_number in range(len(row)) for element in row[image_number][image_row_number]]
                for row in borderless_images for image_row_number in range(len(row[0]))]
    search_image = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
    search_image = list(map(lambda x: list(x), search_image))
    num_monsters = count_monsters(monsters, search_image)
    all_hashes = sum([1 for row in monsters for element in row if element == '#'])
    search_hashes = sum([1 for row in search_image for element in row if element == '#'])
    return all_hashes - (num_monsters * search_hashes)


if __name__ != 'main':
    print(solve_part1(get_input_of_day(20)))
    print(solve_part2(get_input_of_day(20)))
