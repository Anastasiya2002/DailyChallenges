#You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

#Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
def islandPerimeter(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print("For grid " ,i,j)
            if grid[i][j]==1:
              if i != len(grid)-1:
               if grid[i+1][j] == 0:
                   count +=1
              else:
                count += 1
              if i != 0:
                if grid[i-1][j] == 0:
                    count += 1
              else:
                count += 1
              if j != len(grid[i])-1:
                if grid[i][j+1] == 0:
                    count += 1
              else:
                count += 1
              if j != 0:
                if grid[i][j-1]==0:
                 count +=1
              else:
                count +=1
            print(count)
    return count

print(islandPerimeter(
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))
                   