def get_input_of_day(day_number):
    infile = 'tests/data/day' + str(day_number) + 'input.txt'
    input_data = open(infile, 'r')
    my_list = []
    for x in input_data:
        my_list.append(x.strip())
    input_data.close()
    return my_list