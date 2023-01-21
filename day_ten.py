import input_file_reader
import heapq

def solve():
    input_object = input_file_reader.FileReader('input_files/input_day10.txt')
    instructions_list = input_object.read_input_file()

    cycle = 0;
    register_x = 1;
    result = 0

    for instruction in instructions_list:
        cycle += 1;
        # print("Cycle: " + str(cycle))
        # print("Register X: " + str(register_x))
        if (cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
            result += (register_x)*cycle
        if instruction == "":
            continue;

        if instruction == "noop":
            continue;
        
        if instruction.split(" ")[0] == "addx":
            cycle += 1;
            if (cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
                result += (register_x)*cycle
            register_x += int(instruction.split(" ")[1])
    
    return result

answer = solve()
print(answer)
        