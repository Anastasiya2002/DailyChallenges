#Write a function that takes a string as input and reverse only the vowels of a string.
def reverseVowels( s):
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        v = []
        
        for i,x in enumerate(s):
            if x in vowel:
                v.append(i)
        
        s = list(s) # turn a string into a list
        n = len(v)
        for i in range(n//2):
            s[v[i]], s[v[n-1-i]] = s[v[n-1-i]], s[v[i]]
        
        return "".join(s)