import input_file_reader

def get_pairs_data(pairs_input):
    pairs_split = pairs_input.split(",")
    pair_one = pairs_split[0]
    pair_two = pairs_split[1]
    pair_one_split = pair_one.split('-')
    pair_two_split = pair_two.split('-')

    pair_one_start = int(pair_one_split[0])
    pair_one_end = int(pair_one_split[1])
    pair_two_start = int(pair_two_split[0])
    pair_two_end = int(pair_two_split[1])

    return (pair_one_start, pair_one_end, pair_two_start, pair_two_end)


def solve():
    input_object = input_file_reader.FileReader('input_files/input_day4.txt')
    pairs_list = input_object.read_input_file()

    count_of_fully_capsulating_pairs = 0 

    for pairs in pairs_list:
        if (pairs == ''):
            continue
        pair_one_start, pair_one_end, pair_two_start, pair_two_end = get_pairs_data(pairs)
        
        if ((pair_one_start >= pair_two_start) and (pair_one_end <= pair_two_end)):
            count_of_fully_capsulating_pairs += 1 
        elif ((pair_two_start >= pair_one_start) and (pair_two_end <= pair_one_end)):
            count_of_fully_capsulating_pairs += 1
    
    return count_of_fully_capsulating_pairs

def solve_part_two():
    input_object = input_file_reader.FileReader('input_files/input_day4.txt')
    pairs_list = input_object.read_input_file()

    count_of_overlapping_pairs = 0

    for pairs in pairs_list:
        if (pairs == ''):
            continue 
        pair_one_start, pair_one_end, pair_two_start, pair_two_end = get_pairs_data(pairs)

        if ((pair_one_start >= pair_two_start) and (pair_one_end <= pair_two_end)):
            count_of_overlapping_pairs += 1 
        elif ((pair_two_start >= pair_one_start) and (pair_two_end <= pair_one_end)):
            count_of_overlapping_pairs += 1
        elif ((pair_one_start >= pair_two_start) and (pair_one_start <= pair_two_end)):
            count_of_overlapping_pairs += 1
        elif ((pair_one_end >= pair_two_start) and (pair_one_end <= pair_two_end)):
            count_of_overlapping_pairs += 1 

    return count_of_overlapping_pairs     


answer = solve()
print(answer)
answer_two = solve_part_two()
print(answer_two)