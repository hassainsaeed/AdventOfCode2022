import input_file_reader

def solve():
    input_object = input_file_reader.FileReader('input_files/input_day9.txt')
    motions_list = input_object.read_input_file()

    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0

    og_pos = "0,0"
    unique_tail_pos = set()
    unique_tail_pos.add(og_pos)

    for motion in motions_list:
        if (motion == ""):
            continue
        direction = motion.split(" ")[0]
        distance = int(motion.split(" ")[1])

        for i in range(distance):
            if direction == "R":
                head_x = head_x + 1;
            elif direction == "L":
                head_x = head_x - 1;
            elif direction == "U":
                head_y = head_y + 1;
            elif direction == "D":
                head_y = head_y - 1;
            
            # check of head and tail are one apart. If so do nothing
            if ((abs(head_x - tail_x) == 1) or (abs(head_x - tail_x) == 0)) and ((abs(head_y - tail_y) == 1) or (abs(head_y - tail_y) == 0)):
                continue;
            else:
                # If head and tail not one apart, move tail towards head
                # if they are on the same y axis, move tail to head
                if (head_y == tail_y):
                    if (head_x == tail_x + 2):
                        tail_x += 1
                    elif (head_x == tail_x - 2):
                        tail_x -= 1
                # if they are in the same x axis, move tail up/down to head 
                elif (head_x == tail_x):
                    if (head_y == tail_y + 2):
                        tail_y += 1
                    elif (head_y == tail_y - 2):
                        tail_y -= 1
                elif (head_x > tail_x and head_y < tail_y):
                    tail_x += 1
                    tail_y -= 1
                elif (head_x > tail_x and head_y > tail_y):
                    tail_x += 1
                    tail_y += 1
                elif (head_x < tail_x and head_y > tail_y):
                    tail_x -= 1
                    tail_y += 1
                elif (head_x < tail_x and head_y < tail_y):
                    tail_x -= 1
                    tail_y -= 1

            unique_tail_pos.add(str(tail_x) + ',' + str(tail_y))

    return len(unique_tail_pos)

answer = solve()
print(answer)

