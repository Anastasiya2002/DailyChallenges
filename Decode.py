def Decode(s):
    def numDecodings(s):
      for i in range(len(s)-1):
        if i >= 2:
            break
        rest = s[0:i+1]
        if int(rest)<= 26 and int(rest)>0:
            count += numDecodings(s[i+1])
      return count
    count = 0
    return numDecodings(s)

print(Decode('12'))
        


