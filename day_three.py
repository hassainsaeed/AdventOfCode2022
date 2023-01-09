import input_file_reader

def solve():
    rucksack_input_filereader = input_file_reader.FileReader('input_files/input_day3.txt') 
    rucksack_input_list = rucksack_input_filereader.read_input_file();
    total_priority_score = 0;

    for rucksack in rucksack_input_list:
        rucksack_size = len(rucksack)
        rucksack_item_map = {}
        for i in range(rucksack_size):
            if (i < rucksack_size/2):
                rucksack_item_map[rucksack[i]] = 1
            else:
                if (rucksack[i] in rucksack_item_map):
                    if rucksack[i].islower():
                        total_priority_score += ord(rucksack[i]) - 96
                    else:
                        total_priority_score += ord(rucksack[i]) - 64 + 26
                    break

    
    return total_priority_score

def solve_part_two():
    rucksack_input_filereader = input_file_reader.FileReader('input_files/input_day3.txt') 
    rucksack_input_list = rucksack_input_filereader.read_input_file();
    total_priority_score = 0;
    
    num_rucksacks = len(rucksack_input_list)
    index = 0
    
    while index < num_rucksacks-2:
        first_rucksack_item_map = {}
        for item in rucksack_input_list[index]:
            first_rucksack_item_map[item] = 1
        second_rucksack_item_map = {}
        index += 1;
        for item in rucksack_input_list[index]:
            if item in first_rucksack_item_map:
                second_rucksack_item_map[item] = 1
        index += 1
        for item in rucksack_input_list[index]:
            if (item in first_rucksack_item_map) and (item in second_rucksack_item_map):
                if item.islower():
                    total_priority_score += ord(item) - 96
                else:
                    total_priority_score += ord(item) - 64 + 26
                break

        index += 1
    
    return total_priority_score


answer = solve()
print(answer)
answer_two = solve_part_two()
print(answer_two)
            