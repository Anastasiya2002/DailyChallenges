def getMoneySpent(keyboards, drives, b):
    if min(keyboards) + min(drives) > b:
        return "-1"
    sum = 0
    for i in keyboards:
        for j in drives:
            if i + j > sum and i+j <=b:
                sum = i+j
    return sum
