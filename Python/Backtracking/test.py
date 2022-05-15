board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - ' * 3)

        for x in range(len(board[0])):
            if x % 3 == 0 and x != 0:
                print(" | ", end="")

            if x == 8:
                print(board[i][x])

            else:
                print(str(board[i][x]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for x in range(len(board[0])): #For x in range length of each row
            if board[i][x] == 0:
                return (i, x) #row, col

def check(board, num, pos):
    for i in board:
        if i.count(num) == 0

        exit()

# print(find_empty(board))
check(board, 3, (3, 4))