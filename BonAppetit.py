def bonAppetit(bill,k,b):
    bill.remove(bill[k])
    if sum(bill)/2 == b:
        print ("Bon Appetit")
        return
    print((int)(b - sum(bill)/2))

print([3,10,2,9],1,12)


