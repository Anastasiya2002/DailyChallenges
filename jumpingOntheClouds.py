def jumpingOnTheClouds(c):
    position = 0
    count = 0
    done = False
    while position != len(c)-1:
        if position < len(c)-2: 
          if c[position+2] == 0:
            position += 2
            count += 1
            done = True
        if done==False:
            position += 1
            count += 1
        done = False
    return count

print(jumpingOnTheClouds([0,0,0,1,0,0]))

