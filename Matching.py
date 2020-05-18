#Given an input string (s) and a pattern (p),
# implement regular expression matching with support for '.' and '*'.

#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
def isMatch(s,p):
    i = 0
    previus = ""
    for letter in s:
        if i== len(p):
            return False
        print(letter)
        if letter != p[i] and p[i]!="." and ((previus != letter and previus != ".") or p[i] != "*"):
            if i+1< len(p):
              if letter != p[i] and p[i+1] == "*":
                i += 2
                if i < len(p):
                  if letter != p[i] and p[i]!=".":
                    return False
                else:
                    return False
              else:
                 return False
            else:
                return False
        previus = p[i]
        i += 1
    print(i)
    if i <= len(p)-1 and p[-1] != "*":
        print('here')
        return False
    return True
