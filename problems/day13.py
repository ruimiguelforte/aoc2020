from problems.common import get_input_of_day
import math


def process_schedule(input_list):
    now = int(input_list[0].strip())
    buses = input_list[1].strip().split(',')
    return now, buses


def minutes_to_wait(now, bus_id):
    return (bus_id - (now % bus_id)) % bus_id


def is_valid_timestamp(ts, buses_reformatted):
    for minutes, bus_id in buses_reformatted:
        if ((ts + minutes) % bus_id) != 0:
            return False
    return True


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def find_earliest_timestamp(buses, min_timestamp):
    buses_reformatted = [(i, int(bus_id)) for i, bus_id in enumerate(buses) if bus_id != 'x']
    step = 1
    steps = []
    current_timestamp = min_timestamp
    i = 0
    current_bus = buses_reformatted[i]
    while not is_valid_timestamp(current_timestamp, buses_reformatted):
        if ((current_timestamp + current_bus[0]) % current_bus[1]) == 0:
            step = lcm(step, current_bus[1])
            steps.append(step)
            i += 1
            current_bus = buses_reformatted[i]
        current_timestamp += step
    return current_timestamp, len(steps)


def solve_part1(input_list):
    now, buses = process_schedule(input_list)
    waiting_times = {minutes_to_wait(now, int(bus_id)): int(bus_id) for bus_id in buses if bus_id != 'x'}
    min_time = min(waiting_times.keys())
    return min_time * waiting_times[min_time]


def solve_part2(input_list):
    now, buses = process_schedule(input_list)
    current_timestamp, num_steps = find_earliest_timestamp(buses, 1000000)
    return current_timestamp


if __name__ != 'main':
    print(solve_part1(get_input_of_day(13)))
    print(solve_part2(get_input_of_day(13)))
