#Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
def intToRoman(num):
    roman = ["M", "CM", "D","CD","C","XC","L",'XL',"X","IX","V","IV","I"]
    number = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    answer = ""
    while num:
        i= 0
        while i <len(number) and num < number[i]:
            i+= 1
        num= num - number[i]
        answer += roman[i]
    return answer

print(intToRoman(1994))
