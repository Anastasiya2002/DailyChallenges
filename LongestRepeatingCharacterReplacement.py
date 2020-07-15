#Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

#In one operation, you can choose any character of the string and change it to any other uppercase English character.

#Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.
def characterReplacement(s,k):
    count = 0
    i = 1
    while i < len(s): 
        if s[i-1] != s[i]:
           if k > 0:
            if s[i+1] == s[i-1]:
                count += 2
                k -= 1
                s= s[:i] + s[i+1] + s[i] + s[i+2:]
                i+=1
           else:
             break
        else:
             count += 2
             i +=1
        i +=1
    return count

print(characterReplacement('ABAB',2))



