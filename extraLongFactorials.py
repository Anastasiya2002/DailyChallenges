def extraLongFactorials(n):
    if n == 1:
        return n
    else:
       return (extraLongFactorials(n-1) * n)

print(extraLongFactorials(25))