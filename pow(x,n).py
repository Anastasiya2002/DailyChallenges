#Implement pow(x, n), which calculates x raised to the power n (xn).
def myPow(x,n):
    result = calculate(x,abs(n))
    return result if n>= 0 else 1/result

def calculate(x,n):
    if n == 0:
        return 1
    print(x,n)
    return calculate(x*x,n//2) if n%2==0 else x*calculate(x*x,n//2)
print(myPow(2,4))