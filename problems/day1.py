from problems.common import get_input_of_day


def get_pair_that_sum_to(input_list, y):
    my_pair = -1
    p1dic = {}
    for x in input_list:
        p1dic[int(x)] = (y - int(x), p1dic.get(int(x), (0, 0))[1] + 1)

    for k, v in p1dic.items():
        # This checks for a pair with equal values
        if (y % 2 == 0) and (k == y/2) and (v[1] > 1):
            my_pair = (k, k)
            break
        if v[0] in p1dic.keys():
            my_pair = (k, v[0])
            break
    return my_pair


def solve_part1(input_list):
    my_pair = get_pair_that_sum_to(input_list, 2020)
    return my_pair[0] * my_pair[1]


def solve_part2(input_list):
    # Lazily, I brute-forced this
    input_list = sorted(list(map(int, input_list)))
    for i in range(len(input_list) - 2):
        for j in range(1, len(input_list) - 1):
            if (2020 - input_list[i] - input_list[j]) in input_list[j + 1:]:
                return input_list[i] * input_list[j] * (2020 - input_list[i] - input_list[j])


if __name__ != 'main':
    print(solve_part1(get_input_of_day(1)))
    print(solve_part2(get_input_of_day(1)))
