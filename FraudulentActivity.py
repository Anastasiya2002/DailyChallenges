#if the amount spent by a client on a particular day is greater than or equal to  2* the client's median spending for a trailing number of days, 
# they send the client a notification about potential fraud.
def activityNotifications(expenditure, d):
    notification, median = 0,0
    one_day= []
    if d % 2 == 1: odd = True
    else: odd = False
    middle = d//2
    for i in range(d, len(expenditure)):
        one_day= sorted(expenditure[i-d:i])
        if odd:
             median = one_day[middle]
        else:
             median = sum(one_day[middle-1:middle+1])/ 2
        if expenditure[i] >= median* 2:
            notification+=1
    return notification

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)