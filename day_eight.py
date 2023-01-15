import input_file_reader
import copy

# This function parses input, and returns a 2D array of tree heights
def create_tree_grid():
    input_object = input_file_reader.FileReader('input_files/input_day8.txt')
    tree_rows = input_object.read_input_file()
    tree_grid = []

    for tree_row in tree_rows:
        if (tree_row == ''):
            continue
        tree_grid.append([*tree_row])
    
    return tree_grid


def solve():
    tree_grid = create_tree_grid();
    
    num_visible_trees = len(tree_grid[0]) + len(tree_grid[-1]) + 2*(len(tree_grid)-2)

    for y in range(1, len(tree_grid)-1):
        for x in range(1, len(tree_grid[0])-1):
            val = int(tree_grid[y][x])
            if (dfs_one_dir(tree_grid, x+1, y, val,'right')):
                num_visible_trees += 1
            elif (dfs_one_dir(tree_grid, x-1, y, val, "left")):
                num_visible_trees += 1
            elif (dfs_one_dir(tree_grid, x, y+1, val, "up")):
                num_visible_trees += 1
            elif (dfs_one_dir(tree_grid, x, y-1, val, "down")):
                num_visible_trees += 1


    return num_visible_trees;

def dfs_one_dir(grid, x, y, orig_val, direction):
    if ((x == 0) or (x == len(grid[0])-1) or (y == 0) or (y == len(grid)-1)):
        if (orig_val > int(grid[y][x])):
            return True
        else:
            return False
    
    if ((int(grid[y][x]) >= orig_val)):
        return False 
    
    if (direction == "right"):
        return dfs_one_dir(grid, x+1, y, orig_val, direction);
    elif (direction == "left"):
        return dfs_one_dir(grid, x-1, y, orig_val, direction);
    elif (direction == "up"):
        return dfs_one_dir(grid, x, y+1, orig_val, direction);
    else:
        return dfs_one_dir(grid, x, y-1, orig_val, direction);

def solve_part_two():
    tree_grid = create_tree_grid();
    max_score = 1
    for y in range(1,len(tree_grid)-1):
        for x in range(1,len(tree_grid[0])-1):
            val = int(tree_grid[y][x])
            score = dfs_num_trees_blocking(tree_grid,x+1,y,val,"right",0)*dfs_num_trees_blocking(tree_grid,x-1,y,val,"left",0)*dfs_num_trees_blocking(tree_grid,x,y+1,val,"up",0)*dfs_num_trees_blocking(tree_grid,x,y-1,val,"down",0)
            max_score = max(score, max_score)

    return max_score;

def dfs_num_trees_blocking(grid, x, y, orig_val, direction, num_trees):
    if ((x == 0) or (x == len(grid[0])-1) or (y == 0) or (y == len(grid)-1) or (int(grid[y][x]) >= orig_val)):
        return num_trees+1;
    
    if (direction == "right"):
        return dfs_num_trees_blocking(grid, x+1, y, orig_val, direction, num_trees+1);
    elif (direction == "left"):
        return dfs_num_trees_blocking(grid, x-1, y, orig_val, direction, num_trees+1);
    elif (direction == "up"):
        return dfs_num_trees_blocking(grid, x, y+1, orig_val, direction, num_trees+1);
    else:
        return dfs_num_trees_blocking(grid, x, y-1, orig_val, direction, num_trees+1); 


answer = solve();
print(answer);
answer_two = solve_part_two();
print(answer_two);
444528