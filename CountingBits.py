#Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
def countBits(num):
    res = [0]
    while len(res) <= num:
            res += [a + 1 for a in res]
    return res[0:num + 1]
print(countBits(5))
