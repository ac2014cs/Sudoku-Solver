def solve(bo):
#solves a sudoku board using backtracking
#then return solution

    find = find_empty(bo)

    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, pos, num):
#Returns if the attempted move is invalid

#checks the row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos [1] !=i:
            return False

#checks the column
    for i in range(0, len(bo)):
        if bo[pos][1]== num and pos[1] !=i:
            return False

#checks the box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True


def find_empty(bo):
    #finds an empty space in the board

    for i in range(len(bo[0])):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j)
    return None

def print_board(bo):
    #Prints the board

    for i in range(len(bo)):
        if i % 3 == 0 and i !=0:
            print ("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print (bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")