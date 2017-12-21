##table = [[0,0,0,0],
##         [0,0,0,0],
##         [0,0,0,0],
##         [0,0,0,0]]
##random_add(table)
##show_table(table)
##while not game_end(table):
##    d = input('Enter direction code: ')
##    merge(table,d)
##    random_add(table)
##    show_table(table)


import random
points = 0
khopi_attemt = 0
game_box = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
first_position_list = [0,1,2,3]
first_row_to_begin = random.chioce(first_position_list)
first_column_to_begin = random.choice(first_position_list)
game_box[first_row_to_begin][first_column_to_begin] = 2

2 2 0 2     4 2 2 2
2 4 2 0     4 8 4 4
0 4 0 4     0 0 0 8
4 0 4 8     0 0 0 0

2 2 2 2
2 4 4 4
4 4 0 8
0 0 0 0

def up_movement(game_box):
    i = 0
    for j in range(0,4):
        if game_box[i][j] != 0 or game_box[i+j][j] != 0 
