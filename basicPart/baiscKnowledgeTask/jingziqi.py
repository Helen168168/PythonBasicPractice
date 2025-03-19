'''
井字棋
'''
import random
def print_board(board):
    for i in range(3):
        print(' '.join(board[i]))
def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True
def game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    while True:
        print_board(board)
        x, y = map(int, input('请输入坐标: ').split())
        if board[x][y] != ' ':
            print('该位置已经有棋子了')
            continue
        board[x][y] = player
        if check_win(board, player):
            print_board(board)
            print(f'{player}赢了')
            break
        if check_tie(board):
            print_board(board)
            print('平局')
            break
        player = 'O' if player == 'X' else 'X'
game()
