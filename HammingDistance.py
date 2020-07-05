#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

#Given two integers x and y, calculate the Hamming distance.
def hammingDistance(x,y):
    x= convertToBinary(x)
    y = convertToBinary(y)
    count = 0
    if len(x)>len(y):
        diff = len(x)-len(y)
        count= x[:diff].count('1')
        x= x[diff:]
    elif len(x)<len(y):
        diff = len(y)-len(x)
        count= x[:diff].count('1')
        y= y[diff:]
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1
    return count


def convertToBinary(x):
    result = ''
    while x>0:
        if x%2== 0:
            result = "0"+result
        else:
            result = "1"+result
        x = x//2
    return result

print(hammingDistance(1,4))