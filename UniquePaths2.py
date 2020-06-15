#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

#Now consider if some obstacles are added to the grids. How many unique paths would there be?


def uniquePaths(obstacle_grid):
    m_start= 1
    n_start = 1
    m = len(obstacle_grid)
    n = len(obstacle_grid[0])
    return calculate(m_start,n_start,m,n,obstacle_grid)

def calculate(m_start,n_start,m,n,obstacle_grid):
    if obstacle_grid[m_start-1][n_start-1]== 1:
        return 0
    if m_start == m and n_start == n:
        return 1
    if m_start == m:
        return calculate(m_start, n_start+1,m,n,obstacle_grid)
    elif n_start==n:
        return calculate(m_start+1, n_start,m,n,obstacle_grid)
    else:
        return calculate(m_start, n_start+1,m,n,obstacle_grid) +calculate(m_start+1, n_start,m,n,obstacle_grid)

print(uniquePaths([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))