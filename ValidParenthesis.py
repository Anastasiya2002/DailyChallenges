#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#1.Open brackets must be closed by the same type of brackets.
#2.Open brackets must be closed in the correct order.
def isValid(s):
    dict = {'(':")",'{':'}','[':']',')':'-1', "}":'-1',"]":'-1'}
    needed = ' '
    for i in s:
        if i == needed[-1]:
            needed= needed[:len(needed)-1]
        elif dict[i] != '-1':
            needed += dict[i]
        else:
            return False
    if len(needed) != 1:
        return False
    return True
print(isValid("{"))
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("([)]"))
