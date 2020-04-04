def sockMerchant(n,ar):
   dic ={}
   pair = 0
   for i in ar:
       if i not in dic:
           dic[i] = 1
       else:
           dic[i] += 1
           if dic[i] % 2 == 0:
               pair+=1
   return pair

print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20] ))

