#define the largest hourglass
arr= [[1,1,1,0,0,0],
     [1,1,0,0,0,0],
     [1,1,1,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]]

def hourglassSum(arr):
   rows = len(arr[0])
   col = len(arr) 
   sum = 0
   j = 0
   maxsum = 0
   for i in range(col - 2):
    for j in range(rows - 2):
        for moveLeft in range(3):
            for moveDown in range(3):
                if moveDown == 1 and moveLeft != 1:  
                    continue
                else:
                    sum += arr[i+ moveDown][j+moveLeft]
        if(maxsum < sum):
            maxsum = sum
        sum = 0
   return maxsum
     
print(hourglassSum(arr))