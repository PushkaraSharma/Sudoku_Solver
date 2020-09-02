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
        if(i%3==0 and i!=0):
            print("----------------------")
        for j in range(len(board[0])):
            if(j%3==0 and j!=0):
                print("| ",end='')

            if(j==8):
                print(board[i][j])   #if the last element that s8t position then go to next line
            else:
                print(str(board[i][j])+" ",end='') #if not last element then continue ot print in same line

def find_empty_slot(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)    #row and column
    return None

def valid(board,num,pos):
    # check row
    for i in range(len(board[0])):
        if(board[pos[0]][i]==num and pos[1]!=i):
            return False
    #check column
    for i in range(len(board)):
        if(board[i][pos[1]]==num and pos[0]!=i):
            return False
    #check box
    box_x = pos[1]//3
    box_y = pos[0]//3
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if(board[i][j]==num and (i,j)!= pos):
                return False
    return True


def solve(board):

    find = find_empty_slot(board)              #if no empty means solution is find
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(board,i,(row,col)):
            board[row][col]=i                    #if no. is valid place it and call solve again

            if solve(board):
                return True                                     #if false is returned then 0 is placed

            board[row][col]=0

    return  False


# print_board(board)
# solve(board)
# print('****************************')
# print_board(board)