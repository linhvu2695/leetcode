def totalNQueens(n):
    """
    :type n: int
    :rtype: int
    """
    board = [[0]*n for i in range(n)]

    def printBoard(board):
        for row in board:
            print(row)

    def is_not_under_attack(row, col):
        #check horizontal & vertical
        for i in range(n):
            if board[row][i] == 1 or board[i][col] == 1:
                return False
        
        #check diagonals
        for i in range(n):
            for j in range(n):
                if (i-j) == (row-col) or (i+j) == (row+col):
                    if board[i][j] == 1:
                        return False
        
        return True       
                
    def backtrackQueen(row, count):
        for col in range(n):
            if is_not_under_attack(row, col):
                #place a Queen & attacking zone 
                #if the location is not under attack (it wont attack any placed Queen)
                board[row][col] = 1
                
                #if reached last row -> found a solution
                if row == n-1:
                    print('Solution ', count+1)
                    printBoard(board)
                    count += 1
                #if havent reached last row -> continue on next row
                else:
                    count = backtrackQueen(row+1, count)
                
                #remove queen & attacking zone 
                #once found a solution or finish iterating through next row
                board[row][col] = 0
        return count
    
    return backtrackQueen(0, 0)

def main():
    totalNQueens(6)

if __name__ == '__main__':
    main()