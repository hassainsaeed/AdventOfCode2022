import input_file_reader

# This is hard coded based on the input data
# I am sure there is a clevel way to parse the input file and repersent the Stacks as a List of List 
# but I am not a smart man and don't know how, so I figured it was quicker to hard code copy and paste
def gen_stacks():
    # stackA = ['Z','N']
    # stackB = ['M','C','D']
    # stackC = ['P']
    stackA = ['H','C','R']
    stackB = ['B','J','H','L','S','F']
    stackC = ['R','M','D','H','J','T','Q']
    stackD = ['S','G','R','H','Z','B','J']
    stackE= ['R','P','F','Z','T','D','C','B']
    stackF = ['T','H','C','G']
    stackG = ['S','N','V','Z','B','P','W','L']
    stackH = ['R','J','Q','G','C']
    stackI = ['L','D','T','R','H','P','F','S']

    # return [stackA,stackB,stackC]
    return [stackA, stackB, stackC, stackD, stackE,stackF,stackG,stackH,stackI]


def solve():
    input_object = input_file_reader.FileReader('input_files/input_day5.txt')
    instructions_list = input_object.read_input_file()
    stacks = gen_stacks()

    for instruction in instructions_list:
        instruction_split = instruction.split(' ')
        quantity = int(instruction_split[1])
        stack_src = int(instruction_split[3]) - 1
        stack_dest = int(instruction_split[5]) - 1

        for i in range(quantity):
            val = stacks[stack_src].pop()
            stacks[stack_dest].append(val)
        

    final_str = []
    for stack in stacks:
        final_str.append(stack.pop())
    return final_str

def solve_part_two():
    input_object = input_file_reader.FileReader('input_files/input_day5.txt')
    instructions_list = input_object.read_input_file()
    stacks = gen_stacks()

    for instruction in instructions_list:
        instruction_split = instruction.split(' ')
        quantity = int(instruction_split[1])
        stack_src = int(instruction_split[3]) - 1
        stack_dest = int(instruction_split[5]) - 1
        val = stacks[stack_src][-quantity:]
        stacks[stack_dest] += val
        del stacks[stack_src][-quantity:] 

    final_str = []
    for stack in stacks:
        final_str.append(stack.pop())
    return final_str

answer = solve()
print(str(answer))
answer_two = solve_part_two()
print(str(answer_two))
