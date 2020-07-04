#Write a program to find the n-th ugly number.

#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
def nthUglyNumber(n):
    def maxDivide( a, b ): 
       while a % b == 0: 
        a = a / b 
       return a  
  
# Function to check if a number  
# is ugly or not 
    def isUgly( no ): 
      no = maxDivide(no, 2) 
      no = maxDivide(no, 3) 
      no = maxDivide(no, 5) 
      return 1 if no == 1 else 0
    i = 1
    count = 1 # ugly number count 
  
    # Check for all integers untill  
    # ugly count becomes n 
    while n > count: 
        i += 1
        if isUgly(i): 
            count += 1
    return i 

    

print(nthUglyNumber(11))