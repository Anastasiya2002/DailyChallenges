import itertools

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def bt(first,second,ind):
            third=str(int(first)+int(second))
            if len(first)>1 and first.startswith("0") or len(second)>1 and second.startswith("0"):
                return False
            elif ind==n:
                return True
            elif ind+len(third)>n:
                return False
            elif num[ind:ind+len(third)]!=third:
                return False
            else:
                return bt(second,third,ind+len(third))
        n=len(num)
        for i,j in itertools.combinations(range(1,n),2):
            first,second=num[:i],num[i:j]
            if j==n: continue
            if bt(first,second,j):
                return True
        return False