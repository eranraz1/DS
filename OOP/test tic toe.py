#from IPython.display import clear_output
board = [['_','_','_'],['_','_','_'],['_','_','_']]
def display_board():  
    print(f'{board[0]}\n{board[1]}\n{board[2]}')
display_board()


def reset_board():
    board = [['_','_','_'],['_','_','_'],['_','_','_']]


def win_check():
    for i in range(3):
        if board[i] == ['x','x','x'] or board[0:3][i] == ['x','x','x'] or board[i][i] ==['x','x','x']:
            print(1)
            #reset_board()
            return ('player X wins')
        if board[i] == ['0','0','0'] or board[0:3][i] == ['0','0','0'] or board[i][i] ==['0','0','0']:
            #reset_board()
            print(2)
            return ('player y wins')
        else:
            return ('next player - pleae continue ')

def player_input(player,x,y):
    if board[x][y] != '_':
        print('place is hold !!!')
        display_board()
        return 'please try again'
        
    else:
        if player == 1:
            board[x][y] = 'x'
        if player == 2:
            board[x][y] = '0' 
    display_board()
    win_check()

player_input(1,0,2)
player_input(2,1,1)

win_check()
