#You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest 
#number possible given the limit to the number of changes. 
def highestValuePalindrome(s,n,k):
    count_pair = 0
    pair = []
    palindrome_pair = []
    if n == 1:
        return "9"
    for i in range(0, n//2):
        if s[i] != s[n-1-i]:
            count_pair += 1
            pair.append([i,n-1-i])
            s = s[:i] + "9" + s[i+1:(n-1-i)]+ "9" + s[n-i:] 
            k -= 1
            if (s[i] == "0" and s[n-i-1] != "9") or (s[n-1-i] == "0" and s[i] != "9"):
                k -=1
            if  k< 0:
                return "-1"
        elif s[i]!= '9':
            palindrome_pair.append(i)
    found = False
    i = 0
    while k > 0: 
        if k>= 2:
            s = s[:palindrome_pair[i]] + "9" + s[palindrome_pair[i]+1:(n-1-palindrome_pair[i])]+ "9" + s[(n-1-palindrome_pair[i])+1:]
            i += 1 
            k -=2
        if k == 1 and n%2 == 1:
            s = s[:n//2] + "9" + s[n//2+1:]
            k -=1 
        
    return s
print(highestValuePalindrome("0011", 4,1))
    
