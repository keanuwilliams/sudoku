# ---------------------------------------- #
# File:          sudoku.py
# Author:        Keanu Williams
# Description:   Sudoku board and solver  
# Date Created:  October 12, 2021
# Date Modified: October 15, 2021
# ---------------------------------------- #
import random

class Sudoku:

  def __init__(self):
    self.board = self.generatePuzzle()
    self.printBoard()
    self.generateSolution(self.board)

  def shuffle(self, list):
    '''
    Shuffles the given list and returns the same list shuffled
    '''
    return random.sample(list, len(list))

  def findEmptyCell(self, board):
    '''
    Obtain next empty cell in board in the form of a tuple (row, col).
    If there aren't any empty cells in board, None will be returned.
    '''
    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] == 0:
          return (i, j)
    return None

  def isValidPlacement(self, board, value, row, col):
    '''
    Combines existInRow, existInCol, and existInBox to check if the placement of
    the value is valid.
    '''
    return not(self.existInRow(board, value, row) or self.existInCol(board, value, col) or self.existInBox(board, value, row, col))

  def existInRow(self, board, value, row):
    '''
    Returns True if cell value exists within the given row 
    on the Sudoku board, else returns False
    '''
    for i in range(0, 9):
      if value == board[row][i]:
        return True
    return False

  def existInCol(self, board, value, col):
    '''
    Returns True if cell value exists within the given column
    on the Sudoku board, else returns False
    '''
    for i in range(0, 9):
      if value == board[i][col]:
        return True
    return False

  def existInBox(self, board, value, row, col):
    '''
    Finds if cell value exists within its box given row and column
    '''
    
    # Find upper and lower limits for for loops
    rowLimits = self.findUpperLowerLimits(row)
    colLimits = self.findUpperLowerLimits(col)

    #
    for i in range(rowLimits[0], rowLimits[1]): # for each row
      for j in range(colLimits[0], colLimits[1]):
        if value == board[i][j]:
          return True
    return False 

  def findUpperLowerLimits(self, rcIndex):
    '''
    Helper function for existsInBox to find upper and lower limits to be placed into for loop.

    Parameters
    ----------
    rcIndex - row / column index

    Returns
    ----------
    limits - tuple containing the lower and the upper limit in that order
    '''
    upper = 0 # limit not included in for loop
    lower = 0 # limit included in for loop
    if rcIndex < 3:
      upper = 3
      lower = 0
    elif rcIndex < 6:
      upper = 6
      lower = 3
    else:
      upper = 9
      lower = 6
    return (lower, upper)

  def removeNumbers(self, board):
    '''
    Randomly removes numbers to find one unique solution and to
    most importantly finish making the puzzle
    '''

    rounds = random.randint(5, 7)

    for i in range(0, 9):
      for _ in range(1, rounds):
        colToRemove = random.randint(0, 8)
        board[i][colToRemove] = 0


    

  def generateSolution(self, board):
    '''
    Generates a complete solution using Depth First Search (DFS)
    '''
    emptyCell = self.findEmptyCell(board)
    if not emptyCell:
      return True
    
    row, col = emptyCell # get row and col from results of empty cell 
    valid_numbers = self.shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9]) # shuffle the valid numbers
    for num in valid_numbers:
      if self.isValidPlacement(board, num, row, col): # placement of number is valid
        board[row][col] = num # place the valid number on board
        if self.generateSolution(board): # valid solution, end recursion 
          return True
        board[row][col] = 0 # placement is not valid and replace num with 0
    return False # placement is not valid and backtrack
    

  def generatePuzzle(self):
    '''

    Create a new Sudoku board by doing the following algorithm:
    1. Reset the board (board with all zeroes)
    2. Generate a complete solution using Depth First Search (DFS)
    3. Remove numbers from the grid to create the puzzle

    Returns
    ----------
    board - the newly created board with a unique solution

    '''

    # 1. Reset the board
    board = [[0 for i in range(9)] for j in range(9)]
    
    # 2. Use DFS to create a complete solution
    self.generateSolution(board)

    # 3. Remove numbers from the grid to create the puzzle
    self.removeNumbers(board)

    return board
  
  def printBoard(self):
    '''
    Prints the current Sudoku board.
    '''
    row_count = 0 # used to print horizontal dividers
    col_count = 0 # used to print vertical dividers
    for row in self.board:
      
      if row_count == 3 or row_count == 6: # print horizontal dividers at appropriate row
        for _ in range(30):
          print('-', end='')
      print() # print new line

      for col in row: # go through each column in a row
        if col_count == 3 or col_count == 6: # print vertical dividers at appropriate column
          print('|', end='')
        if col != 0: # print number if column isn't empty
          print(f' {col} ', end='')
        else: # print placeholder if column is empty
          print(' _ ', end='')
        col_count += 1
      print() # print new line
      col_count = 0 # reset column count to begin next row
      row_count += 1
    print() # print new line
  
  

if __name__ == '__main__':
  sudoku = Sudoku()
  sudoku.printBoard()
