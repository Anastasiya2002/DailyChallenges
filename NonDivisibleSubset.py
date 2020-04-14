#Complete the nonDivisibleSubset function in the editor below. It should return an integer representing 
#the length of the longest subset that meets the criteria.

def nonDivisibleSubset(k,s):
    maxCount= 0
    new_arr = []
    for i in range(len(s)):
        arr= s[:i]+s[i+1:]
        new_arr.append(s[i])
        for j in arr:
            check =True
            for l in new_arr:
                if (j+l)% k == 0:
                    check = False
            if check:     
               new_arr.append(j)
        if len(new_arr) > maxCount:
            maxCount= len(new_arr)
            print(new_arr)
        new_arr=[]
    return maxCount

if __name__ == '__main__':
   

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)

