def timeInWords(h,m):
    numbers = [
        "zero", 
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine"]
    if m == 00:
        return numbers[h]+ " o' clock"
    if m > 30:
        m = 60 - m
        if m == 15:
            return "quarter to " + numbers[h+1]
        return numbers[m] + " minutes to " +numbers[h+1]
    elif m == 30:
        return "half past " + numbers[h]
    elif m == 15:
        return "quarter past " + numbers[h]
    elif m== 1:
        return "one minute past " + numbers[h]
    return numbers[m]+ " minutes past "+numbers[h]
