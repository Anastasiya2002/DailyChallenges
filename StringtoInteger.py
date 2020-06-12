#Implement atoi which converts a string to an integer.

#The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

#The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

#If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

#If no valid conversion could be performed, a zero value is returned.
def atoi(str):
        dict = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,"7":7,'8':8,'9':9}
        result = 0
        negative = False
        found = False
        new_str= ''
        for i in range(len(str)):
           if str[i] == " ":
                if found:
                 break
           elif str[i]==".":
               break
           elif str[i] not in dict:
               if str[i] == "-":
                   negative = True  
                   found = True
               else: 
                found = True
                break
           else:
               found = True
               new_str += str[i]
        multiply = 10** (len(new_str)-1)
        if len(str)== 1:
            return dict[str] if not negative else -dict[str]
        for i in new_str:
            result = multiply* dict[i] + result
            multiply= multiply//10
        if result > 2**31-1:
            result = 2**31-1 if not negative else 2**31
        return result if not negative else -result


print(atoi("      -987"))

