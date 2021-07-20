#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the paths function below.

count = 0
longestPathLength = 0
longestPath = []
allIncreasingPaths = []
path = []

def paths(grid):
    #base case
    if(len(grid)>1):
        if( len(grid[0])==1 and len(grid[1])==1):
            return 0
    
    global count
    global longestPathLength 
    global longestPath
    global allIncreasingPaths
    
    
    
    rowCount = 0
    columnCount = 0
    
    #Get the dimensions of our grid
    rowCount = len(grid)
    columnCount = len(grid[0])
    
    #loop over every index in 2D grid and find each increasing path
    for i in range(rowCount):
        for j in range(columnCount):
            solve(i,j,grid,columnCount,rowCount)

    print("Finished. Longest path: ", longestPath, "of length: ", longestPathLength)
    print("there are a total of ", count , "increasing paths..")
    print("all increasing paths : ", allIncreasingPaths)


    #if you want unique INC paths, this code can be uncommented...
    # unique = set()
    # for i in allIncreasingPaths:
    #     toAdd = tuple(i)
    #     unique.add(toAdd)
    # print("there are a total of ", len(unique) , " unique increasing paths")
    # print("all unique increasing paths: ",unique)

    longestPath=[]
    longestPathLength=0
    allIncreasingPaths = []
    count = 0
    return 0
    
def solve(x,y,grid,columnCount,rowCount):
    global count 
    global path
    global longestPathLength
    global longestPath
    
    if( x+1 < rowCount ):
        if(grid[x][y] < grid[x+1][y]):

            if len(path)==0:
                path.append(grid[x][y])
                path.append(grid[x+1][y])
            else:
                path.append(grid[x+1][y])

            count = count+1
            allIncreasingPaths.append(path.copy())
            solve(x+1,y,grid,columnCount,rowCount)

    if( y+1 < columnCount):
        if( grid[x][y] < grid[x][y+1] ):

            if len(path)==0:
                path.append(grid[x][y])
                path.append(grid[x][y+1])
            else:
                path.append(grid[x][y+1])
            
            count = count+1
            allIncreasingPaths.append(path.copy())
            solve(x,y+1,grid,columnCount,rowCount)
            
    if( x-1 >= 0 ):
        if( grid[x][y] < grid[x-1][y] ):

            if len(path)==0:
                path.append(grid[x][y])
                path.append(grid[x-1][y])
            else:
                path.append(grid[x-1][y])

            count = count+1
            allIncreasingPaths.append(path.copy())
            solve(x-1,y,grid,columnCount,rowCount)

    if( y-1 >= 0):
        if( grid[x][y] < grid[x][y-1] ):
        
            if len(path)==0:
                path.append(grid[x][y])
                path.append(grid[x][y-1])
            else:
                path.append(grid[x][y-1])

            count = count+1
            allIncreasingPaths.append(path.copy())
            solve(x,y-1,grid,columnCount,rowCount)
    
    if len(path) > longestPathLength:
        longestPathLength = len(path)
        longestPath = path

    path = []
                
            
if __name__ == '__main__':
    
    #2X3 Grid
    paths([[3,4,5],
           [3,2,6]])
         
    #3X3 Grid

    paths([[9,9,4],
           [6,6,8],
           [2,1,1]])
    # 14 increasing paths: [1,2],[1,6],[1,8],[4,8],[4,9],[2,6],[6,9],[6,9],[6,8],[1,2,6],[1,6,8],[1,6,9],[2,6,9],[1,2,6,9]
           
    paths([[3,4,5],
           [3,2,6],
           [2,2,1]])
    # other test case: [[3,4,5],[3,2,6],[2,2,1]] with longest path [3, 4, 5, 6]

    #6X6 Grid
            #[0,0]
    paths([ [3,4,5,9,9,4],
            [3,6,6,7,2,6],
            [1,2,4,2,2,1],
            [9,9,3,6,5,4],
            [6,1,4,6,7,8],
            [1,3,2,1,3,4]])
            #[5,0]

            #longest path at [5,3],[5,2],[4,2],[]

   