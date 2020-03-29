#A left rotation operation on an array shifts 
a=[1,2,3,4,5]
d = 2
def rotLeft(a,d):
   for shift in range(d):
       firstElement = a[0]
       for element in range(len(a)-1):
           a[element] = a[element+1]
       a[len(a)-1]= firstElement   
   return a     

a=[1,2,3,4,5]
d = 2
print(rotLeft(a,d))   

a= [2,3,6,7,9,0,2,8,9,5]
d = 4
print(rotLeft(a,d))