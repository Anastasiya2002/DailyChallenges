def longestPalindrome(s):
    if len(s)==0:
        return ""
    max_word=s[0]
    for i in range(len(s)):
        count = s.count(s[i], i+1)
        print(count)
        index = s.find(s[i], i+1)
        if index != -1:
            for j in range(count):
              word = s[i:index+1]
              if word == word[::-1]:
                  if len(word) > len(max_word):
                     max_word = word
              index = s.find(s[i],index+1)
    return max_word
print(longestPalindrome("ccc"))


