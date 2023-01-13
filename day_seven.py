import input_file_reader
import heapq

# Reads input file command list
# Returns a map of all the file directories (with full dir name) and their size
def get_dir_to_size_map():
    input_object = input_file_reader.FileReader('input_files/input_day7.txt')
    commands_list = input_object.read_input_file()

    # Use a stack to keep track of what folder we're in. First element is dir '/'
    # when we "cd x" we push on the stack. When we "cd .." we pop the stack
    # Also use a map that maps the full dir path to its size
    # every time we see a new dir, add its full path to the map 
    # (we use full path, not dir name, b/c dir name is not unique and can repeat many times)
    # When we see a file, use the stack and the map to add its size to the map for every dir in the stack
    # that way each dir path in the map contains a cumulative sum of all the files under it

    cd_stack = ['/']
    dir_to_size_map = {'/': 0} # 

    for command in commands_list:
        command_split = command.split(" ")
        if command_split[0] == "$":
            if command_split[1] == "cd":
                if command_split[2] == "/":
                    cd_stack = ['/']
                elif command_split[2] == "..":
                    cd_stack.pop()
                else:
                    cd_stack.append(command_split[2])
            elif command_split[1] == "ls":
                continue;
        elif command_split[0] == "dir":
            full_dir_path = '/'.join(cd_stack) + '/' + command_split[1]
            dir_to_size_map[full_dir_path] = 0 
        elif command_split[0].isnumeric():
            # size 
            for i in range(len(cd_stack)):
                    full_dir_path = '/'.join(cd_stack[:i+1])
                    dir_to_size_map[full_dir_path] += int(command_split[0])
    
    return dir_to_size_map


def solve():
    # Iterate through all the keys / dirs in the map
    # for any under 100K, add their size together in a running sum and return
    dir_to_size_map = get_dir_to_size_map()
    sum_of_dir_over_1000 = 0

    for directory in dir_to_size_map:
        # print("Dir name: " + directory + " , size: " + str(dir_to_size_map[directory]))
        if  dir_to_size_map[directory] <= 100000:
            sum_of_dir_over_1000 += dir_to_size_map[directory]
    
    return sum_of_dir_over_1000


def solve_part_two():
    # Need a running total of the entire folder size ---> that is '/' in your dict
    # Need to subtract 70M from size of '/' ---> this is your remaning space
    # Need to subtract 30M from remaining space ---> that is your target 
    # iterate through dict, for any directory greater than your target add to a min heap
    # return lowest value of the min heap
    dir_to_size_map = get_dir_to_size_map()
    current_size = dir_to_size_map['/']
    remaining_space = 70000000 - current_size
    target_space_to_free = 30000000 -  remaining_space

    min_heap = []
    heapq.heapify(min_heap)

    for directory in dir_to_size_map:
        if dir_to_size_map[directory] >= target_space_to_free:
            heapq.heappush(min_heap, dir_to_size_map[directory])

    return heapq.heappop(min_heap)

answer = solve()
print(answer)
answer_two = solve_part_two()
print(answer_two)