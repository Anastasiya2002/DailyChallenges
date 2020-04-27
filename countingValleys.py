def countingValleys(n,s):
    first = False
    count = 0
    valleys= 0
    for i in s:
      if i =="U":
          count += 1
          if first and count == 0:
              valleys += 1
              first =False
      if i=="D":
          count -= 1
          if count < 0:
              first = True
    return valleys
print(countingValleys(8,"UDDDUDUU"))


