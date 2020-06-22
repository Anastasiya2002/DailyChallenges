#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

def wordBreak(s,wordDict):
    if len(wordDict)==0:
        return False
    new_wordDict = {}
    for i in range(len(s)):
        for j in range(len(s[i:])):
            print
            if s[i:j+i+2] in wordDict:
                new_wordDict[s[i:j+i+2]]=1
                break
    return len(new_wordDict)==len(wordDict)

print(wordBreak("applepenapple",["apple", "pen"]))



