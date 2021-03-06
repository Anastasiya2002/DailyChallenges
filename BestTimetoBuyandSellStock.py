#You are given an array prices for which the ith element is the price of a given stock on day i.
#Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
def maxProfit(prices):
    if len(prices) == 1 or len(prices)==0:
        return 0
    x = min(prices)
    y = max(prices)
    ind_1= prices.index(x)
    ind_2 = prices.index(y)
    if ind_1 < ind_2 and len(prices[ind_1:ind_2])!=0:
        return max((y-x)+maxProfit(prices[:ind_1])+maxProfit(prices[ind_2+1:]),maxProfit(prices[ind_1:ind_2])+maxProfit(prices[prices.index(max(prices[ind_1:ind_2]),ind_1,ind_2)+1:ind_2+1]))
    elif ind_1<ind_2 and len(prices[ind_1:ind_2])==0:
        return (y-x)+maxProfit(prices[:ind_1])+maxProfit(prices[ind_2+1:])
    elif len(prices[ind_1:ind_2])!=0:
        return  maxProfit(prices[:ind_1])+maxProfit(prices[ind_2+1:])+maxProfit(prices[ind_1+1:ind_2+1])+maxProfit(prices[max(prices[ind_1:ind_2])+1:ind_2+1])
    else:
        return  maxProfit(prices[:ind_1])+maxProfit(prices[ind_2+1:])


print(maxProfit([5,4,3,2,1])) #-> returns 0
print(maxProfit([7,1,5,3,6,4])) #-> return 7
print(maxProfit([1,2,3,4,5])) #->return 4

