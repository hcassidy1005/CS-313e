class State:
    
    def __init__(self, grid, row, col, endRow, endCol, targetVal, currentVal, gridRows, gridCols, history):
        self.grid = grid
        self.currentRow = row
        self.currentCol = col
        self.history = history
        self.endRow = endRow
        self.endCol = endCol
        self.targetValue = targetVal
        self.currentValue = currentVal
        self.gridRows = gridRows
        self.gridCols = gridCols

    def changeGrid(self, row, col, value):
        # changes position in grid to a different value 
        self.grid[int(row)][int(col)] = value

    def __str__(self): # returns string of the current state (need to fix formating)
        tab = "   "
        gridstring = ""
        for r in range(self.gridRows): # traverse through rows of grid
            gridstring += "\n      "
            for c in range(self.gridCols): # traverse through columns in each row
                gridstring += str(self.grid[r][c])
                if self.grid[r][c] == "X": # spaces for X
                    gridstring += "    "
                elif int(self.grid[r][c]) < 10: # spaces for 1 digit nums
                    gridstring += "    "
                elif int(self.grid[r][c]) < 100: # spaces for 2 digit nums
                    gridstring += "   "
                else: # spaces for 3 digit nums 
                    gridstring += " "
        return tab + "Grid:" + gridstring + "\n" +  tab + "history:" + str(self.history) + "\n" + tab + "start point: (" + str(self.currentRow) + "," + str(self.currentCol) + ")" +"\n" + tab + "sum so far: " + str(self.currentValue) +"\n"

def isValidMove(state, row, col):
    if row < 0 or col < 0 or row >= state.gridRows or col >= state.gridCols: # if its in the boundaries of the maze
        return False
    elif state.grid[row][col] == "X": # if there isn't a bread crumb there 
        return False
    else: 
        return True 

def solve(thisState):
   # this will recursively solve a maze represented by thisState
   print("Is this a goal state?") 
   if thisState.currentValue == thisState.targetValue and thisState.endRow == thisState.currentRow and thisState.endCol == thisState.currentCol:
      print("Yes!") 
      return thisState.history # the maze is solved :)
    
   elif thisState.currentValue > thisState.targetValue: # if the sum has gone too high
        print("Target exceeded:  abandoning path")
        
        # need to figure out how to remove X from wrong path and value from history
        # current value backtracks but grid and history do not... so what is the problem? what is different between the two?
        # if only the Xs would just go away when backtracking then it would find the solution and not get stuck :(
        
        
   else: # still need to do work to solve the maze
      print("No.")
      print("Can I move right?") 
      if isValidMove(thisState, thisState.currentRow, thisState.currentCol + 1): # moving right valid
         print("Yes!")
         print("Paused... \n")
         # create a new State one space right 
         newState = State(thisState.grid, thisState.currentRow, thisState.currentCol + 1, thisState.endRow, thisState.endCol, thisState.targetValue, thisState.currentValue, thisState.gridRows, thisState.gridCols, thisState.history) 
         # append the new location to the state history
         newState.history.append(newState.grid[newState.currentRow][newState.currentCol])
         # add to the sum 
         newState.currentValue = thisState.currentValue + int(newState.grid [newState.currentRow] [newState.currentCol])
         # change the current position in the grid to a x
         newState.changeGrid(newState.currentRow, newState.currentCol, "X")
         print("Problem is now:")
         print(newState) # (for debugging purposes)

         result = solve(newState)
         if result != None:
               return newState.history

      print("No.")
      print("Can I move up?") 
      if isValidMove(thisState, thisState.currentRow - 1, thisState.currentCol): # Moving up is valid
         print("Yes!")
         print("Paused... \n")
         # create a new State one space up
         newState = State(thisState.grid, thisState.currentRow - 1, thisState.currentCol, thisState.endRow, thisState.endCol, thisState.targetValue, thisState.currentValue, thisState.gridRows, thisState.gridCols, thisState.history)
         # append the new location to the state history
         newState.history.append(newState.grid[newState.currentRow][newState.currentCol])
         # add to the sum 
         newState.currentValue = thisState.currentValue + int(newState.grid [newState.currentRow] [newState.currentCol])
         # change the current position in the grid to a X
         newState.changeGrid(newState.currentRow, newState.currentCol, "X")
         print("Problem is now:")
         print(newState) # (for debugging purposes)

         result = solve(newState) # recursively keep solving 
         if result != None:
               return newState.history
            
      print("No.")
      print("Can I move down?") 
      if isValidMove(thisState, thisState.currentRow + 1, thisState.currentCol): # moving down is valid
         print("Yes!")
         print("Paused... \n")
         # create a new State one space down 
         newState = State(thisState.grid,thisState.currentRow + 1,thisState.currentCol, thisState.endRow, thisState.endCol, thisState.targetValue, thisState.currentValue, thisState.gridRows, thisState.gridCols, thisState.history)
         # append the new location to the state history
         newState.history.append(newState.grid[newState.currentRow][newState.currentCol])
         # add to the sum 
         newState.currentValue = thisState.currentValue + int(newState.grid [newState.currentRow] [newState.currentCol])
         # change the current position in the grid to a x
         newState.changeGrid(newState.currentRow, newState.currentCol, "X")
         print("Problem is now:")
         print(newState) # (for debugging purposes)

         result = solve(newState) # recursively keep solving 
         if result != None:
               return newState.history
            
      print("No.")
      print("Can I move left?") 
      if isValidMove(thisState, thisState.currentRow, thisState.currentCol - 1): # moving left valid
         print("Yes!")
         print("Paused... \n")
         # create a new State one space left
         newState = State(thisState.grid, thisState.currentRow, thisState.currentCol - 1, thisState.endRow, thisState.endCol, thisState.targetValue, thisState.currentValue, thisState.gridRows, thisState.gridCols, thisState.history) 
         
         # append the new location to the state history
         newState.history.append(newState.grid[newState.currentRow][newState.currentCol])
         # add to the sum 
         newState.currentValue = thisState.currentValue + int(newState.grid [newState.currentRow] [newState.currentCol])
         # change the current position in the grid to a x
         newState.changeGrid(newState.currentRow, newState.currentCol, "X")
         print("Problem is now:")
         print(newState) # (for debugging purposes)

         result = solve(newState)
         if result != None:
               return newState.history
     

      print("Couldn't move in any direction.  Backtracking.")
      
      return None


def main():

   f = open("MazeData.txt", "r") # opens text for reading file
   line = f.readline() # reads a line
   commandList = line.split() # splits line up at spaces into list

   # read the number of rows, number of columns, startRow, and startCol
   targetValue = int(commandList[0])
   grid_rows = int(commandList[1])
   grid_cols = int(commandList[2])
   start_row = int(commandList[3])
   start_col = int(commandList[4])
   end_row = int(commandList[5])
   end_col = int(commandList[6]) 

   # read in the grid
   grid = []
   line = f.readline() # move on to next line
   rowList = []
   while line != "":
       inputList = line.split()                                                   
       grid.append(inputList)
       line = f.readline()

   # set up start state
   thisState = State(grid, start_row, start_col, end_row, end_col, targetValue, 0, grid_rows, grid_cols, []) # create a new State object
   thisState.history.append(thisState.grid[start_row][start_col]) # add starting point to history 
   thisState.currentValue = int(thisState.grid [start_row][start_col]) # add starting point to sum 
   thisState.changeGrid(start_row, start_col, 'X') # mark the current position with a X
   print(thisState) # for debugging purposes 
                                                        

   result = solve(thisState)    # result will be None or the goal state's history

   if result == None:
      print("No solution exists")
   else:
      print("The solution is: ",result)

main()
