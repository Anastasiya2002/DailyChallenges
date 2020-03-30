#You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] 
#without any duplicates. You are allowed to swap any two elements. 
#You need to find the minimum number of swaps required to sort the array in ascending order.
def minimumSwaps(arr):
    count = 0
    for i in range (len(arr)):
        while(arr[i]!= i +1):
            temp = arr[i]
            arr[i] = arr[temp-1]
            arr[temp-1] = temp
            count += 1
    return count  

print(minimumSwaps([1,3,5,2,4,6,7]))
print(minimumSwaps([4,3,1,2]))
print(minimumSwaps([2,3,4,1,5]))


