def isHappy(n):
     if n == 1:
        return True
     if n >= 0 and n < 10:
         return False
     result = 0
     for i in str(n):
       result += int(i)**2
     isHappy(result)
    
print(isHappy(19))


def bro(n):
        result = n
        new = 0
        while True:
                while result>0:
                    new += (result // 10)**2 + 
                 result= new
                 new = 0
                 if result ==1:
                    return True
        return False