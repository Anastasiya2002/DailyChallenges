#Output the pairs of elements with the smallest difference. If there are multiple pairs, output all of them in ascending order, all on the same line with just a single space between each pair of numbers. A number may be par
#of two pairs when paired with its predecessor and its successor.
def closestNumber(arr):
    arr.sort()
    max_difference= arr[1]-arr[0]
    diff = []
    for i in range(len(arr)-1):
        difference = arr[i+1] - arr[i]
        if difference < max_difference:
            max_difference= difference
            diff = arr[i],arr[i+1]
        elif difference == max_difference:
            diff+= arr[i], arr[i+1]
    
    return list(diff)

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumber(arr)

    print(result)

    

            

