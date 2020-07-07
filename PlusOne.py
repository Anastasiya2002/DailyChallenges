#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

#You may assume the integer does not contain any leading zero, except the number 0 itself.

def plusOne(digits):
    carrier = 0
    for i in range(len(digits)-1,-1,-1):
        if carrier == 0 and digits[i]+1<= 9:
            digits[i] += 1 +carrier
            break
        elif digits[i]+carrier <= 9 and carrier != 0:
            digits[i]+= carrier
            break
        else:
            if carrier == 0:
               digits[i] += 1 +carrier
            else:
                digits[i]+= carrier
            carrier= digits[i]//10
            digits[i] = digits[i]% 10 
            if i == 0 and carrier != 0:
                digits.insert(0,carrier)
    return digits

print(plusOne([9,9]))
        
