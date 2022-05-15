board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def find_empty(board):
    for i in range(len(board)):
        for x in range(len(board[i])):
            if board[i][x] == 0:
                return (i, x)

def check(board, value, pos):
    row = pos[0]
    col = pos[1]

    for i in range(len(board)):
        board[row][col] = value

check(board, 1, find_empty(board))
print(board)