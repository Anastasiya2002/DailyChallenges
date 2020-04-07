import math
def squares(a,b):
    count = 0
    i = 0
    contin= True
    while contin:
        if i**2 >= a and i**2<=b:
            count += 1
        if i**2>b:
            contin = False
        i+=1
    return count

        


print(squares(3,9))
