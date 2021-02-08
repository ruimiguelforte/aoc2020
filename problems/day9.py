from problems.common import get_input_of_day


def process_numbers(input_list):
    numbers = []
    for line in input_list:
        clean = line.strip()
        if clean != '':
            numbers.append(int(clean))
    return numbers


def solve_part1(input_list, preamble):
    numbers = process_numbers(input_list)
    i = 1
    possible_sums = {}
    source = {}
    while i < len(numbers):
        # Get the current number
        current_number = numbers[i]
        # If we are not in the preamble, check if we found the culprit
        if i >= preamble and current_number not in possible_sums:
            break
        # If we are not in the preamble remove the number preamble positions ago
        if (i - preamble) >= 0:
            remove_number = numbers[i - preamble]
            sums_to_check = source[remove_number]
            del source[remove_number]
            for test_sum in sums_to_check:
                possible_sums[test_sum].remove(remove_number)
                possible_sums[test_sum].remove(test_sum - remove_number)
                if len(possible_sums[test_sum]) == 0:
                    del possible_sums[test_sum]
                source[test_sum - remove_number].remove(test_sum)
                if len(source[test_sum - remove_number]) == 0:
                    del source[test_sum - remove_number]
        # Add in the new number
        source[current_number] = {(numbers[x] + current_number) for x in range(max(0, i - preamble), i)}
        for possible_sum in source[current_number]:
            if possible_sum not in possible_sums:
                possible_sums[possible_sum] = {current_number, possible_sum - current_number}
            else:
                possible_sums[possible_sum] = possible_sums[possible_sum].union(
                    {current_number, possible_sum - current_number})

            if (possible_sum - current_number) not in source:
                source[possible_sum - current_number] = {possible_sum}
            else:
                source[possible_sum - current_number].add(possible_sum)
        i += 1
    return current_number


def solve_part2(input_list, preamble):
    numbers = process_numbers(input_list)
    target_number = solve_part1(input_list, preamble)
    for i in range(len(numbers)):
        current_sum = 0
        desired_numbers = []
        j = i
        while (j < len(numbers)) and (current_sum < target_number):
            current_sum += numbers[j]
            desired_numbers.append(numbers[j])
            j += 1
        if current_sum == target_number:
            break
    return min(desired_numbers) + max(desired_numbers)


if __name__ != 'main':
    print(solve_part1(get_input_of_day(9), 25))
    print(solve_part2(get_input_of_day(9), 25))
