def balancedsum(arr):
    n = len(arr)
    i = 0
    j = n-1
    left = 0
    right = 0
    while  i < n and j >= 0:
            if ( left == right and i == j):
                return "YES"
            if ( left > right):
                right += arr.get(j)
                j-=1
            else:
                left += arr.get(i)
                i+=1
    if left == right:
      return "YES"
    return "NO"