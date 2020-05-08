#There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.
def maximumToys(prices, k):
    count = 0
    while k>=0:
        k -= min(prices)
        prices.remove(min(prices))
        count += 1
    count -= 1
    return count
print(maximumToys([1,12,5,111,200,1000,10], 50))

