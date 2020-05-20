#Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
def romanToINt(s):
    count = 0
    dict = {"I": 1,"V": 5, "X": 10, "L":50, "C":100,"D":500, "M": 1000}
    previous = ""
    for i in s:
        if ((i == "X" or i == "V" )and previous =="I") or ((i == "L" or i == "C") and previous =="X") or ((i == "M" or i == "D" )and previous =="C"):
            count += dict[i]-2*dict[previous]
        else:
            count += dict[i]
        previous = i
    return count
print(romanToINt("LVIII"))