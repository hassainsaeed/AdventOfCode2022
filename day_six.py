import input_file_reader

def analyze_signal(num_characters):
    input_object = input_file_reader.FileReader('input_files/input_day6.txt')
    signal_input = input_object.read_input_file()[0]
    # signal_input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" 

    if len(signal_input) < num_characters:
        # This should not be possible. But if this does happen, return None
        return None

    # First lets get the first four elements of the signal
    # put them in a Dict to confirm uniqueness 
    # if all unique (len of dict == num_chars) - hooray we can return
    
    unique_char_set = {}
    start_window = 0
    end_window = num_characters - 1
    list_of_char_seen = []

    for i in range(num_characters):
        unique_char_set[signal_input[i]] = 1
    
    if (len(unique_char_set) == num_characters):
        return num_characters
    
    # If not all elements unique, slide the window by 1 to the right
    # put all these elements in the sliding window into a new Dict to confirm uniqueness
    # if all unique (len of dict == num_chars) - hooray we can return end_window position + 1
    # if not, keep sliding window one to the right until we do
    
    while ((len(unique_char_set) < num_characters) and (end_window < len(signal_input))):
        # print(len(unique_char_set))
        unique_char_set = {}
        start_window += 1
        end_window += 1
        for i in range(start_window, end_window+1):
            unique_char_set[signal_input[i]] = 1

    return end_window + 1


def solve():
    return analyze_signal(4)

def solve_part_two():
    return analyze_signal(14)

answer = solve()
print(answer)
answer_two = solve_part_two()
print(answer_two)