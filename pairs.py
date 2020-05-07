#You will be given an array of integers and a target value. Determine the number of pairs of 
#array elements that have a difference equal to a target value.
def pairs(k,arr):
    count = 0
    i, j = 0,1
    arr.sort()
    while j < len(arr):
        diff = arr[j]-arr[i]
        if diff == k:
            count += 1
            j+= 1
        elif diff>k:
            i+=1
        elif diff< k:
            j +=1
    return count

print(pairs(2,[1,5,3,4,2]))