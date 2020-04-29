import math
def encryption(s):
    s= s.replace(" ", "")
    row= math.floor(len(s)**0.5)
    column= math.ceil(len(s)**0.5)
    while row*column < len(s):
        row+= 1
    result = []
    for i in range(row):
        result.append(s[:column])
        s=s[column:]
    res= ""
    for i in range(column):
        for j in result:
            if i < len(j):
               res += j[i]   
        res+=" "
    return res
    
print(encryption("feed the dog"))