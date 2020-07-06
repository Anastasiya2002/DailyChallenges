#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

#Given two integers x and y, calculate the Hamming distance.
def hammingDistance(x,y):
    count = 0
    while max(x,y)>0:
        if x>0 and y >0:
           if (x%2== 0 and y%2== 1 )or  (x%2== 1 and y%2== 0 ):
            count += 1
           x = x//2
           y = y//2
        else:
            if x <=0 :
                 if y%2 == 1:
                    count += 1
                 y=y//2
            else:
                if x%2 ==1:
                    count +=1
                x = x//2
        
                
    return count

print(hammingDistance(1,4))