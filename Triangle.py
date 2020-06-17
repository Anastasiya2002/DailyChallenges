#Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
def minimumTotal(triangle) :
    result = 0
    for tr in triangle:
        tr.sort()
        needed = tr[0]
        result += needed
    return result

print(minimumTotal([[-1],[2,3],[1,-1,-3]]))  