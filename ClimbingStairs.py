#You are climbing a stair case. It takes n steps to reach to the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def climbingStairs(n):
    if n < 2:
        return 1
    return climbingStairs(n-1) +climbingStairs(n-2)


print(climbingStairs(38))
    