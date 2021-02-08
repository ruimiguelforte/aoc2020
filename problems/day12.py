from problems.common import get_input_of_day


def process_directions(input_list):
    directions = []
    for line in input_list:
        clean = line.strip()
        if clean != '':
            directions.append((clean[0], int(clean[1:])))
    return directions


def get_new_direction(facing, left_or_right, amount):
    compass_directions = ('E', 'S', 'W', 'N')
    current_pos = compass_directions.index(facing)
    steps = amount / 90
    if left_or_right == 'L':
        steps *= -1
    new_pos = current_pos + steps
    return compass_directions[int(new_pos % 4)]


def move_ship(facing, north, east, action, amount):
    if action == 'E':
        return facing, north, east + amount
    if action == 'W':
        return facing, north, east - amount
    if action == 'N':
        return facing, north + amount, east
    if action == 'S':
        return facing, north - amount, east
    if action == 'F':
        return move_ship(facing, north, east, facing, amount)
    else:
        return get_new_direction(facing, action, amount), north, east


def get_new_waypoint_direction(waypoint_north, waypoint_east, action, amount):
    if action == 'L':
        amount = 360 - amount
    steps = int((amount / 90) % 4)
    if steps == 1:
        return -waypoint_east, waypoint_north
    if steps == 2:
        return -waypoint_north, -waypoint_east
    if steps == 3:
        return waypoint_east, -waypoint_north
    return waypoint_north, waypoint_east


def move_ship_and_waypoint(ship_north, ship_east, waypoint_north, waypoint_east, action, amount):
    if action == 'E':
        return ship_north, ship_east, waypoint_north, waypoint_east + amount
    if action == 'W':
        return ship_north, ship_east, waypoint_north, waypoint_east - amount
    if action == 'N':
        return ship_north, ship_east, waypoint_north + amount, waypoint_east
    if action == 'S':
        return ship_north, ship_east, waypoint_north - amount, waypoint_east
    if action == 'F':
        return ship_north + waypoint_north * amount, ship_east + waypoint_east * amount, waypoint_north, waypoint_east
    else:
        new_waypoint_north, new_waypoint_east = get_new_waypoint_direction(waypoint_north, waypoint_east, action,
                                                                           amount)
        return ship_north, ship_east, new_waypoint_north, new_waypoint_east


def solve_part1(input_list):
    directions = process_directions(input_list)
    current_position = ('E', 0, 0)
    for direction in directions:
        current_position = move_ship(*current_position, *direction)
    return abs(current_position[1]) + abs(current_position[2])


def solve_part2(input_list):
    directions = process_directions(input_list)
    ship_position = (0, 0)
    waypoint_position = (1, 10)
    for direction in directions:
        coordinates = move_ship_and_waypoint(*ship_position, *waypoint_position, *direction)
        ship_position = coordinates[0:2]
        waypoint_position = coordinates[2:]
    return abs(ship_position[0]) + abs(ship_position[1])


if __name__ != 'main':
    print(solve_part1(get_input_of_day(12)))
    print(solve_part2(get_input_of_day(12)))
