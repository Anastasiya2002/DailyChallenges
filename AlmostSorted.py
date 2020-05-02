#given an array of integers determine whether the array can be sorted in ascending order
#using only one of the following operation
#1. swap two elements
#2. reverse one sub0segment
def almostSorted(arr):
    first,found= 0,False
    second,count = 0,0
    swap = False
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            count += 1
            arr = arr[:i]+arr[i+1:i+2]+ arr[i:i+1]+ arr[i+2:]
            if arr[i-1] > arr[i]:
                swap = True
            if not found:
               first = i
               found = True
        elif found:
            second = i
            found = False
    if found:
        second = len(arr)-1
    if count == 0:
        print("yes")
    elif count - (second-first) == 0:
        print("yes")
        if swap:
           print("swap",first+1,second+1)
        else:
           print("reverse", first+1, second+1)
    else:
        print("no")
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)