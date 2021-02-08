from problems.common import get_input_of_day


def process_jolts(input_list):
    jolts = []
    for line in input_list:
        clean = line.strip()
        if clean != '':
            jolts.append(int(clean))
    return jolts


def count_combinations(current_adaptor, remaining_adaptors):
    combinations_cache = {}

    def get_cache_key(current_adaptor, remaining_adaptors):
        return str(current_adaptor) + "." + ".".join(map(str, remaining_adaptors))

    def count_helper(current_adaptor, remaining_adaptors):
        if remaining_adaptors == []:
            return 1

        # DP check
        key = get_cache_key(current_adaptor, remaining_adaptors)
        if key in combinations_cache:
            return combinations_cache[key]

        first_remaining_adaptor = remaining_adaptors[0]
        if first_remaining_adaptor - current_adaptor > 3:
            return 0
        elif first_remaining_adaptor - current_adaptor == 3:
            count = count_helper(first_remaining_adaptor, remaining_adaptors[1:])
        else:
            count = count_helper(first_remaining_adaptor, remaining_adaptors[1:]) + \
                    count_helper(current_adaptor, remaining_adaptors[1:])
        combinations_cache[key] = count
        return count

    return count_helper(current_adaptor, remaining_adaptors)


def solve_part1(input_list):
    jolts = process_jolts(input_list)
    sorted_jolts = sorted(jolts)
    sorted_jolts = [0] + sorted_jolts + [max(sorted_jolts) + 3]
    jolt_differences = [sorted_jolts[i] - sorted_jolts[i - 1] for i in range(1, len(sorted_jolts))]
    return len([x for x in jolt_differences if x == 1]) * len([x for x in jolt_differences if x == 3])


def solve_part2(input_list):
    jolts = process_jolts(input_list)
    sorted_jolts = sorted(jolts)
    sorted_jolts = [0] + sorted_jolts + [max(sorted_jolts) + 3]
    return count_combinations(0, sorted_jolts[1:])


if __name__ != 'main':
    print(solve_part1(get_input_of_day(10)))
    print(solve_part2(get_input_of_day(10)))
