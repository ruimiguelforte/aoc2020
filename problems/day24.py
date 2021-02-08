from problems.common import get_input_of_day


def process_input(input_list):
    tiles = []
    for line in input_list:
        clean = line.strip()
        if clean != '':
            directions = []
            i = 0
            while i < len(clean):
                current_char = clean[i]
                if current_char in ('n', 's'):
                    directions.append(clean[i:i + 2])
                    i += 2
                else:
                    directions.append(clean[i])
                    i += 1
            tiles.append(directions)
    return tiles


def direction_switch(direction):
    dmap = {
        'ne': (1, 0),
        'sw': (-1, 0),
        'se': (0, 1),
        'nw': (0, -1),
        'e': (1, 1),
        'w': (-1, -1)
    }
    return dmap.get(direction, "Unknown direction!")


def get_unique_tile(directions):
    ne = 0
    se = 0
    for direction in directions:
        ne_add, se_add = direction_switch(direction)
        ne += ne_add
        se += se_add
    return ne, se


def get_tile_map(tiles):
    tile_map = {}
    for directions in tiles:
        tile = get_unique_tile(directions)
        tile_map[tile] = tile_map.get(tile, 0) + 1
    return tile_map


def count_tiles(tiles):
    tile_map = get_tile_map(tiles)
    return sum([1 for value in tile_map.values() if value % 2 == 1])


def solve_part1(input_list):
    tiles = process_input(input_list)
    return count_tiles(tiles)


def count_adjacent_black_tiles(black_tiles, tile, dmap):
    adjacent = 0
    for ne_add, se_add in dmap.values():
        if (tile[0] + ne_add, tile[1] + se_add) in black_tiles:
            adjacent += 1
    return adjacent


def get_next_black_tiles(black_tiles, min_ne, max_ne, min_se, max_se, dmap):
    new_black_tiles = set()
    for ne in range(min_ne - 1, max_ne + 2):
        for se in range(min_se - 1, max_se + 2):
            tile = (ne, se)
            adjacent = count_adjacent_black_tiles(black_tiles, tile, dmap)
            if tile in black_tiles:
                if 1 <= adjacent <= 2:
                    new_black_tiles.add(tile)
            else:
                if adjacent == 2:
                    new_black_tiles.add(tile)
    return new_black_tiles, min_ne - 1, max_ne + 1, min_se - 1, max_se + 1


def get_black_tiles_after_n(black_tiles, min_ne, max_ne, min_se, max_se, n, dmap):
    for _ in range(n):
        black_tiles, min_ne, max_ne, min_se, max_se = get_next_black_tiles(black_tiles, min_ne, max_ne, min_se, max_se,
                                                                           dmap)
    return black_tiles


def solve_part2(input_list):
    tiles = process_input(input_list)
    tile_map = get_tile_map(tiles)
    starting_black_tiles = {key for key, value in tile_map.items() if value % 2 == 1}
    min_ne = min([x for x, _ in starting_black_tiles])
    max_ne = max([x for x, _ in starting_black_tiles])
    min_se = min([x for _, x in starting_black_tiles])
    max_se = max([x for _, x in starting_black_tiles])
    dmap = {
        'ne': (1, 0),
        'sw': (-1, 0),
        'se': (0, 1),
        'nw': (0, -1),
        'e': (1, 1),
        'w': (-1, -1)
    }
    return len(get_black_tiles_after_n(starting_black_tiles, min_ne, max_ne, min_se, max_se,100, dmap))


if __name__ != 'main':
    print(solve_part1(get_input_of_day(24)))
    print(solve_part2(get_input_of_day(24)))
