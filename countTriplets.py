def countTriplets(arr,r):
    new_arr = [r**i for i in range (len(arr))]
    count = 0
    for i in arr:
        if i in new_arr:
            ind = new_arr.index(i)
            if ind < len(new_arr)-2:
             if new_arr[ind+1] in arr:
                 if new_arr[ind+2] in arr:
                     count += arr.count(new_arr[ind+1 ])
                     count += arr.count(new_arr[ind+2])-1
                     
    return count

print(countTriplets([1,3,9,9,27,81], 3))


