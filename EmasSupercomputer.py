#Given a grid of size n*m, each cell in the grid is either  or .
#A valid plus is defined here as the crossing of two segments (horizontal and vertical) of equal lengths. These lengths must be odd, and the middle cell of its horizontal segment must cross the middle cell of its vertical segment.
#Find the two largest valid pluses that can be drawn on good cells in the grid, 
#and return an integer denoting the maximum product of their areas. In the above diagrams, our largest pluses have areas of  and . The product of their areas is .
#B stands for a bad cell G for good
def twoPluses(grid):
    count = 0
    final_count = 1
    unit = 0
    area= []
    arr=[[]]
    for i in range(len(grid)):
        new_word = grid[i]
        for letter in range(len(new_word)):
            if new_word[letter] == "G":
              index_i = i
              index_j= letter
              while index_i >0:
                  index_i -=1
                  word = grid[index_i]
                  if word[letter] =="G":
                      if [index_i,letter] in arr:
                           break
                      count +=1
                  else:
                      break
              if count != 0:
               unit = count
               count = 0
               index_i = i
               while index_i < len(grid)-1:
                   index_i+= 1
                   word = grid[index_i]
                   if word[letter] =="G":
                       if [index_i,letter] in arr:
                           break
                       count +=1
                   else:
                      break
               if count != 0:
                    if count < unit:
                         unit = count
                    count = 0
                    while index_j > 0:
                        index_j -= 1
                        if new_word[index_j] == "G":
                           if [i,index_j] in arr:
                                break
                           count += 1
                        else:
                           break
                    if count != 0:
                           if count < unit:
                             unit = count
                           index_j= letter
                           count = 0
                           while index_j <len(new_word)-1:
                                index_j+=1
                                if new_word[index_j] == "G":
                                   if [i,index_j] in arr:
                                              break
                                   count += 1
                                else:
                                    break
                           if count != 0:
                               if count < unit:
                                   unit = count
                               for j in range(unit):
                                   arr.append([i+j,letter])
                                   arr.append([i-j, letter])
                                   arr.append([i,letter+j])
                                   arr.append([i,letter-j])
                               area+=[(unit * 4) + 1]
              count = 0
    if len(area)> 1: 
           final_count *= max(area)
           area.pop(area.index(max(area)))
           final_count *= max(area)
    if len(area)==1:
            final_count *= max(area)


    return final_count
                


print(twoPluses(["GGGGGG","GBBBGB","GGGGGG","GGBBGB","GGGGGG"]))
print(twoPluses(["BGBBGB","GGGGGG","BGBBGB","GGGGGG","BGBBGB","BGBBGB"]))
print(twoPluses(["GGGGGGGGG","GBBBGGBGG","GBBBGGBGG","GBBBGGBGG","GBBBGGBGG","GBBBGGBGG","GBBBGGBGG","GGGGGGGGG"]))
