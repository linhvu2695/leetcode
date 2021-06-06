def displayBoard(board):
    for i in range(9):
        for j in range(9):
            if j%3 == 2:
                print(board[i][j], '|', end=' ')
            else:
                print(board[i][j], end=' ')
        print()
        if i == 2 or i == 5:
            print(('- - -   - - -   - - -'))
    print('END')

def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    def nextCandidate(row, col):
        new_row = row
        new_col = col
        found = False
        
        while new_row < 9:
            for i in range(9):
                if board[new_row][i] == '.':
                    new_col = i
                    found = True
                    break
            if found:
                break
            else:
                #search nex row
                new_row += 1
        
        return new_row, new_col

    def isValid(row, col, num):
        #check row & column
        for i in range(9):
            if board[row][i] == num:
                if i != col:
                    return False
            if board[i][col] == num:
                if i != row:
                    return False

        #check square 3x3
        for i in range(row//3*3, row//3*3 + 3):
            for j in range(col//3*3, col//3*3 + 3):
                if board[i][j] == num:
                    if i != row or j != col:
                        return False

        return True
                
    def backtrackSudoku(row, col, blank_count):
        for num in range(1, 10):
            if isValid(row, col, num):
                #place candidate
                board[row][col] = num
                blank_count -= 1
                
                if blank_count != 0:
                    #backtrack next_candidate
                    next_row, next_col = nextCandidate(row,col)
                    blank_count = backtrackSudoku(next_row, next_col, blank_count)

                if blank_count != 0:
                    #remove candidate
                    board[row][col] = '.'
                    blank_count += 1
        return blank_count

    #convert board
    for i in range(9):
        for j in range(9):
            if board[i][j].isdigit():
                board[i][j] = int(board[i][j])

    #count numbers of blanks
    blank_count = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                blank_count += 1

    #search first blank
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                backtrackSudoku(i, j, blank_count)
                break
        break

    return board



board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

print('Original Sudoku:')
displayBoard(board)

print('Solution:')
displayBoard(solveSudoku(board))