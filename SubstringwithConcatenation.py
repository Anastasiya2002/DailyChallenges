def findSubString(s,words):
    add= len(words[0])
    i = 0
    found=[]
    start = []
    copy = words.copy()
    while i < len(s)-1:
        if s[i:i+add] in copy:
                copy.remove(s[i:i+add])
                start.append(i)
                i+= add
        elif s[i:i+add] in words:
                if len(copy)== 0:
                   found.append(start[0])
                copy = words
                start=[i]
                i+= add
        else:
            i+=1
    if len(found)== 0:
        return []
    if start[0] != found[-1]:
        found.append(start[0])
    if start[-1]+add== len(s) and found[0]== 0:
        return []
    return found

print(findSubString("wordgoodgoodgoodbestword",["word","good","best","word"],))



