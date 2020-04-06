#You have a string of lowercase English alphabetic letters. 
# You can perform two types of operations on the string:

#Append a lowercase English alphabetic letter to the end of the string.
#Delete the last character in the string. Performing this operation on an empty string results in an empty string.

#Note that you can delete from an empty string as many times as you want
def AppendAndDelete(s,t,k):
    count = 0
    for i in range(len(s), -1,-1):
        for j in range(len(t),-1,-1):
            if s[:i] == t[:j]:
                count += len(t[j:])
                if len(s[i:])== 0 and count != k:
                    if (k- count) % 2 == 1:
                         return "No"
                    return "Yes"
                elif count <= k - len(s[i:]):
                    return "Yes"
                else:
                    return "No"
    if len(s) + len(t) ==k:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input())

    print(AppendAndDelete(s, t, k))



