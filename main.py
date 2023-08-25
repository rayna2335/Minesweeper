"""Minesweeper Board Creator: this program uses 2D arrays to display the grid with mines.

Written by: Ayar Maw, Rayna Maruyama (Group 9)
Date: September 8, 2022
Functions:
place_mines(board, mines) - Generates random row and column and places a mine anywhere on the board.
count_mines(board) - Checks the surrounding 8 spaces to count the number of mines.
display_board(board) - Displays the contents of the board
"""

import check_input
import random

def place_mines(board, mines):
  """Function that randomly places the mines into the board
  Args:
    Prompts: Places a mine using loops to go through each rows and colomns.
  Returns:
    '0' for empty spaces and 'X' for mines into the board
  """
  
  #length of the board that user inputs
  row_length = len(board)
  col_length = len((board[0]))

  # iteranation to place mines
  while mines > 0:
      #set random mines on the board
      rand_row = random.randrange(row_length)
      random_col = random.randrange(col_length)

      #check if there is no mine yet
      if board[rand_row][random_col] == '0':
          board[rand_row][random_col] = 'X'
          mines -= 1
     



def count_mines(board):
  """Function that counts the number of mines 
  Args:
    Prompts: For every row and column it checks if there is a mine. If there is a mine, then it checks the sourounding for more mines and counts.
  Returns:
    The counted number of mines 
  """
  row = len(board)
  col = len(board[0])

  # iteration to put the values in each row and column
  for x in (range(row)):
    for y in (range(col)):
      count = 0 # to count the numbers of mines

      # to check the mines in the neighbor
      for i in (range(x - 1, x + 2)):
        for j in (range(y - 1, y + 2)):

            # to check whether out of range
            if i >= 0 and i < row and j >= 0 and j < col:
                # mine found
                if board[i][j] == 'X':
                    count += 1
      # if it is not a mine                
      if board[x][y] != 'X':
          board[x][y] = count #update the value



def display_board(board):
  """Function that displays the board
    Prompts: For every row and colomn, it displays the value to '0'
  Returns:
    The empty board
  """
  #setting the length of board
  row = len(board)
  column = len(board[0])

  # 2D matrix of 0's (x = current row and y = current column)
  for x in range(0, row):
    for y in range(0, column):
        print(board[x][y], end = " ")
    print()

  return board #return board





def main():
  print("Minesweeper Maker")

  #input from the user size of board
  rows = check_input.get_int_range("Enter number of rows (5-10): ", 5, 10)
  columns = check_input.get_int_range("Enter number of column (5-10): ", 5, 10)
  num_mines = check_input.get_int_range("Enter number of mines (5-10): ", 5, 10)

  #set up a empty board with rows and columns
  board = [['0' for x in range(rows)] for y in range(columns)]
 
  # use 2d board coordinates from display_board() function
  place_mines(board, int(num_mines))
  count_mines(board)
  display_board(board)






main()

