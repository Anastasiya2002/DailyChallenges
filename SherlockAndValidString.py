#Sherlock considers a string to be valid if all characters 
# of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index 
# in the string, and the remaining characters will occur the same number of times. Given a s
#determine if it is valid. If so, return YES, otherwise return NO.
import collections
def isValid(s):
    frequency = collections.Counter(s)
    other_values = []
    max_frequency= 0
    values = list(frequency.values())
    for value in values:
          freq = values.count(value)
          if freq > len(values)//2:
              max_frequency = value
              if len(values)- freq > 1:
                  return "NO"
              if len(values)== freq:
                  return "YES"
          else:
              other_values.append(value)
    if max_frequency != 0:
       if other_values[0] - max_frequency != 1 and other_values[0]!= 1:
            return "NO"
       return "YES"
    return "NO"
        
        
print(isValid("abbccc"))
