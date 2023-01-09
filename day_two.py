import input_file_reader

def read_input_file():
    file_input = open('input_day2.txt', 'r')
    read_file = file_input.read()
    parsed_input = read_file.split('\n')
    return parsed_input

def solve():
    input_object = input_file_reader.FileReader('input_files/input_day2.txt')
    input = input_object.read_input_file()
    player1_score_map = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    player2_score_map = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    total_score = 0
    for game in input:
        game_score = 0
        moves = game.split(' ')
        if (len(moves) < 2):
            continue
        player1_move = moves[0]
        player2_move = moves[1]
        player1_score = player1_score_map[player1_move]
        player2_score = player2_score_map[player2_move]
        if (player1_score == player2_score):
            game_score += 3;
        elif ((player1_score == 1 and player2_score == 2) or (player1_score == 2 and player2_score == 3) or (player1_score == 3 and player2_score == 1)):
            game_score += 6;
        else:
            game_score += 0
        
        game_score += player2_score
        total_score += game_score

    return total_score

def solve_part_two():
    input_object = input_file_reader.FileReader('input_files/input_day2.txt')
    input = input_object.read_input_file()
    player1_score_map = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    player2_score_map = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    total_score = 0
    for game in input:
        game_score = 0
        moves = game.split(' ')
        if (len(moves) < 2):
            continue
        player1_move = moves[0]
        player1_score = player1_score_map[player1_move]
        outcome = moves[1]
        if (outcome == 'X'):
            if player1_score == 1:
                player2_score = 3;
            elif player1_score == 2:
                player2_score = 1;
            elif player1_score == 3:
                player2_score = 2;
            game_score += 0;
        elif (outcome == 'Y'):
            player2_score = player1_score
            game_score += 3;
        else:
            if player1_score == 1:
                player2_score = 2;
            elif player1_score == 2:
                player2_score = 3;
            elif player1_score == 3:
                player2_score = 1;
            game_score += 6;

        game_score += player2_score
        total_score += game_score

    return total_score


answer = solve()
print(answer)
answer_two = solve_part_two()
print(answer_two)