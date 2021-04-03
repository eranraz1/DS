#from IPython.display import clear_output
board = [['_','_','_'],['_','_','_'],['_','_','_']]
def display_board(bp):  
    print(f'{bp[0]}\n{bp[1]}\n{bp[2]}')
display_board(board)


def reset_board(bp):
    bp = [['_','_','_'],['_','_','_'],['_','_','_']]
    return bp


def win_check(bp):
    for i in range(3):
        if bp[i] == ['x','x','x'] or bp[0:3][i] == ['x','x','x'] or bp[i][i] ==['x','x','x']:
            print('reset')
            #reset_board(bp)
            bp = [['_','_','_'],['_','_','_'],['_','_','_']]
            print ('player X wins')
           
        if bp[i] == ['0','0','0'] or bp[0:3][i] == ['0','0','0'] or bp[i][i] ==['0','0','0']:
            reset_board(bp)
            print('reset')
            print ('player y wins')
            return bp
        else:
            print ('next player - pleae continue ')
            return bp
def check_exist(func):
    def wrapper(x,y,bp = board):
          if bp[x][y] != '_':
            print('place is hold !!!')
            display_board(bp)
            return 'please try again'    



def player_input(player,x,y,bp = board):
    # if bp[x][y] != '_':
    #     print('place is hold !!!')
    #     display_board(bp)
    #     return 'please try again'       
    # else:
    if player == 1:
        bp[x][y] = 'x'
    if player == 2:
        bp[x][y] = '0' 
    display_board(bp)
    win_check(bp)
    return bp

board = [['x','x','x'],['x','x','x'],['x','x','x']]
display_board(board)
board = player_input(1,2,2)
board = player_input(2,1,1)

board = win_check(board)
