#You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#Given n, find the total number of full staircase rows that can be formed.
def arrangeCoins(n):
    i = 1
    if n == 1:
        return i
    while n-i>=0:
        n -= i
        i+= 1
    return i-1

print(arrangeCoins(8))