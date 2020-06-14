#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#How many possible unique paths are there?
def uniquePaths(m,n):
    m_start= 1
    n_start = 1
    return calculate(m_start,n_start,m,n)

def calculate(m_start,n_start,m,n):
    if m_start == m and n_start == n:
        return 1
    if m_start == m:
        return calculate(m_start, n_start+1,m,n)
    elif n_start==n:
        return calculate(m_start+1, n_start,m,n)
    else:
        return calculate(m_start, n_start+1,m,n) +calculate(m_start+1, n_start,m,n)

print(uniquePaths(3,2))
print(uniquePaths(7,3))

