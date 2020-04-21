def maxProfit(prices):
    profit = 0
    while len(prices)!= 0 and len(prices)!= 1:
       maximum = max(prices)
       minimum = min(prices)
       if prices.index(minimum) < prices.index(maximum):
           arr = prices[prices.index(minimum)+1:prices.index(maximum)]
           if prices.index(max(arr)) > prices.index(minimum) and  prices.index(min(arr)) < prices.index(maximum) and prices.index(min(arr)) >  prices.index(max(arr)):
               if maximum - minimum < max(arr) - minimum + maximum - min(arr):
                   profit += max(arr) - minimum + maximum - min(arr)  
               else:
                   profit += maximum - minimum
           else:
                profit += maximum - minimum
           prices = prices[:prices.index(minimum)]+prices[prices.index(maximum)+1:]
       else:    
           prices.remove(maximum)
    return profit
print(maxProfit([6,1,3,2,4,7]))