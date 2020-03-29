#define the largest hourglass
arr= [[-1,-1,0,-9,-2,-2],
     [-2,-1,-6,-8,-2,-5],
     [-1,-1,-1,-2,-3,-4],
     [-1,-9,-2,-4,-4,-5],
     [-7,-3,-3,-2,-9,-9],
     [-1,-3,-1,-2,-4,-5]]

def hourglassSum(arr):
   rows = len(arr[0])
   col = len(arr) 
   sum = 0
   j = 0
   maxsum = arr[0][0] + arr[0][1] + arr[0][2] + arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2]
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