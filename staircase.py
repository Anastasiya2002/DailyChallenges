def miniMaxSum(arr):
    larg= 0
    smal = 0
    found1,found2 = False,False
    for i in arr:
        if i != min(arr) or found1:
            larg+= i
        else:
            found1= True
        if i != max(arr) or found2:
            smal+= i
        else:
            found2 = True
        
    print(smal,larg)


miniMaxSum([1,2,3,4,5])