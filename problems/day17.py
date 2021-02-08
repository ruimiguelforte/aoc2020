from problems.common import get_input_of_day


def set_state_3d(pocket, x, y, z, state):
    if z not in pocket:
        pocket[z] = {}
    if y not in pocket[z]:
        pocket[z][y] = {}
    pocket[z][y][x] = state
    return pocket


def get_state_3d(pocket, x, y, z):
    if (z in pocket) and (y in pocket[z]) and (x in pocket[z][y]):
        return pocket[z][y][x]
    return '.'


def count_active_neighbours_3d(pocket, x, y, z):
    neighbours = [get_state_3d(pocket, i, j, k) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) for k in
                  range(z - 1, z + 2) if i != x or j != y or k != z]
    return len([x for x in neighbours if x == '#'])


def get_next_step_3d(pocket, min_x, max_x, min_y, max_y, min_z, max_z):
    new_pocket = {}
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                current_state = get_state_3d(pocket, x, y, z)
                active_neighbours = count_active_neighbours_3d(pocket, x, y, z)
                if current_state == '#':
                    new_state = '#' if 1 < active_neighbours < 4 else '.'
                else:
                    new_state = '#' if active_neighbours == 3 else '.'
                set_state_3d(new_pocket, x, y, z, new_state)
    return new_pocket, min_x - 1, max_x + 1, min_y - 1, max_y + 1, min_z - 1, max_z + 1


def execute_n_steps_3d(pocket, min_x, max_x, min_y, max_y, min_z, max_z, n):
    for i in range(n):
        pocket, min_x, max_x, min_y, max_y, min_z, max_z = get_next_step_3d(pocket, min_x, max_x, min_y, max_y, min_z,
                                                                            max_z)
    return pocket


def count_active_3d(pocket):
    return (len([get_state_3d(pocket, x, y, z) for z in pocket for y in pocket[z] for x in pocket[z][y] if
                 get_state_3d(pocket, x, y, z) == '#']))


def process_input_3d(input_list):
    pocket = {}
    z = 0
    y = 0
    for line in input_list:
        clean = line.strip()
        if clean != '':
            elements = list(clean)
            for x in range(len(elements)):
                pocket = set_state_3d(pocket, x, y, z, elements[x])
            y += 1
    return pocket


def set_state_4d(pocket, x, y, z, w, state):
    if w not in pocket:
        pocket[w] = {}
    if z not in pocket[w]:
        pocket[w][z] = {}
    if y not in pocket[w][z]:
        pocket[w][z][y] = {}
    pocket[w][z][y][x] = state
    return pocket


def get_state_4d(pocket, x, y, z, w):
    if (w in pocket) and (z in pocket[w]) and (y in pocket[w][z]) and (x in pocket[w][z][y]):
        return pocket[w][z][y][x]
    return '.'


def count_active_neighbours_4d(pocket, x, y, z, w):
    neighbours = [get_state_4d(pocket, i, j, k, l) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) for k in
                  range(z - 1, z + 2) for l in range(w - 1, w + 2) if i != x or j != y or k != z or l != w]
    return len([x for x in neighbours if x == '#'])


def get_next_step_4d(pocket, min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w):
    new_pocket = {}
    for w in range(min_w - 1, max_w + 2):
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                for z in range(min_z - 1, max_z + 2):
                    current_state = get_state_4d(pocket, x, y, z, w)
                    active_neighbours = count_active_neighbours_4d(pocket, x, y, z, w)
                    if current_state == '#':
                        new_state = '#' if 1 < active_neighbours < 4 else '.'
                    else:
                        new_state = '#' if active_neighbours == 3 else '.'
                    set_state_4d(new_pocket, x, y, z, w, new_state)
    return new_pocket, min_x - 1, max_x + 1, min_y - 1, max_y + 1, min_z - 1, max_z + 1, min_w - 1, max_w + 1


def execute_n_steps_4d(pocket, min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w, n):
    for i in range(n):
        pocket, min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w = get_next_step_4d(pocket, min_x, max_x, min_y,
                                                                                          max_y, min_z, max_z, min_w,
                                                                                          max_w)
    return pocket


def count_active_4d(pocket):
    return (len(
        [get_state_4d(pocket, x, y, z, w) for w in pocket for z in pocket[w] for y in pocket[w][z]
         for x in pocket[w][z][y] if get_state_4d(pocket, x, y, z, w) == '#']))


def process_input_4d(input_list):
    pocket = {}
    w = 0
    z = 0
    y = 0
    for line in input_list:
        clean = line.strip()
        if clean != '':
            elements = list(clean)
            for x in range(len(elements)):
                pocket = set_state_4d(pocket, x, y, z, w, elements[x])
            y += 1
    return pocket


def solve_part1(input_list):
    pocket = process_input_3d(input_list)
    new_pocket = execute_n_steps_3d(pocket, 0, len(input_list[0]), 0, len(input_list), 0, 0, 6)
    return count_active_3d(new_pocket)


def solve_part2(input_list):
    pocket = process_input_4d(input_list)
    new_pocket = execute_n_steps_4d(pocket, 0, len(input_list[0]), 0, len(input_list), 0, 0, 0, 0, 6)
    return count_active_4d(new_pocket)


if __name__ != 'main':
    print(solve_part1(get_input_of_day(17)))
    print(solve_part2(get_input_of_day(17)))
