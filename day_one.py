
import heapq
import input_file_reader


def solve():
    input_object = input_file_reader.FileReader('input_files/input_day1.txt')
    calorie_list = input_object.read_input_file()
    
    # Set min heap
    # set running sum (int)
    # loop through all calories in list
    # if current input is empty, add running sum, multiply by -1, add to min heap and set running sum to 0
    # else add to running sum
    # return final value
    heap = []
    heapq.heapify(heap)
    total_calories = 0

    for calorie in calorie_list:
        if (calorie.isdigit() is False):
            heapq.heappush(heap, (total_calories*-1))
            total_calories = 0 
        else:
            total_calories += int(calorie)

    return heapq.heappop(heap)*-1

def solve_part_two():
    input_object = input_file_reader.FileReader('input_files/input_day1.txt')
    calorie_list = input_object.read_input_file()
    
    # Set min heap
    # set running sum (int)
    # loop through all calories in list
    # if current input is empty, add running sum, multiply by -1, add to min heap and set running sum to 0
    # else add to running sum
    # after finishing list, run a loop of 3 to get the three highest calories and sum them up
    # return final value
    heap = []
    heapq.heapify(heap)
    total_calories = 0

    for calorie in calorie_list:
        if (calorie.isdigit() is False):
            heapq.heappush(heap, (total_calories*-1))
            total_calories = 0 
        else:
            total_calories += int(calorie)

    sum_of_top_three = 0;
    for i in range(3):
        sum_of_top_three += heapq.heappop(heap)*-1
    return sum_of_top_three 

answer = solve()
print(answer)
answer_two = solve_part_two()
print(answer_two)