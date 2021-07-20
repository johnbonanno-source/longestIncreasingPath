#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the paths function below.
count = None

def paths(grid):
    #base case
    if(len(grid)>1):
        if( len(grid[0])==1 and len(grid[1])==1):
            return 0
    
    global count 
    count = 0
    
    rowCount = 0
    columnCount = 0
    
    for row in grid:
        rowCount = rowCount+1
    for i in grid[0]:
        columnCount = columnCount+1
    

    for i in range(rowCount):
        for j in range(columnCount):
            solve(i,j,grid,columnCount,rowCount)
    return count
    
def solve(x,y,grid,columnCount,rowCount):
    global count 
    
    if( x+1 < rowCount ):
        
        if(grid[x][y] < grid[x+1][y]):
            print(grid[x][y], grid[x+1][y])
            count = count+1
            solve(x+1,y,grid,columnCount,rowCount)

    if( y+1 < columnCount):
        if( grid[x][y] < grid[x][y+1] ):
            print(grid[x][y], grid[x][y+1])

            count = count+1
            solve(x,y+1,grid,columnCount,rowCount)
            
    if( x-1 >= 0 ):
        if( grid[x][y] < grid[x-1][y] ):
            print(grid[x][y], grid[x-1][y-1])

            count = count+1
            solve(x-1,y,grid,columnCount,rowCount)

    if( y-1 >= 0):
        if( grid[x][y] < grid[x][y-1] ):
            print(grid[x][y], grid[x][y-1])

            count = count+1
            solve(x,y-1,grid,columnCount,rowCount)
          
    


                
            
if __name__ == '__main__':
    print(paths(
    [[9,9,4],
     [6,6,8],
    [ 2,1,1]]
    ))