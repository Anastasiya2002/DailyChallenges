def countAndSay(n):
    if n == 1:
            return str(1)  # base case 
    else:
            result = []
            count = 0
            # get previous string
            print('Passing n', n)
            pre = countAndSay(n-1)
            print('Checking', pre)
            letter = pre[0]
            for i in range(len(pre)):
                if pre[i] != letter:
                    result.append(str(count))
                    result.append(letter)

                    count = 1
                    letter = pre[i]
                else:
                    count += 1
                # in case end with out appending
                if i == len(pre) - 1:
                    result.append(str(count))
                    result.append(letter)
            print('here')
            return ''.join(result)

print(countAndSay(5))  

