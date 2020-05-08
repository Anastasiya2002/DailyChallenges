def countSwaps(a):
    found = True
    swaps = 0
    while found:
        found = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swaps += 1
                element = a[i]
                a[i] = a[i+1]
                a[i+1]= element
                found = True
    print("Array is sorted in",swaps, "swaps.")
    print("First Element:",a[0])
    print("Second Element:", a[len(a)-1])

countSwaps([3,2,1])