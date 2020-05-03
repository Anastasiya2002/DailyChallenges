#In this challenge you need to print the string that accompanies each integer in a list sorted by the integers. If two strings are associated with the same integer, they must be printed in their original order so your sorting algorithm should be stable. There is one other twist. 
#The first half of the strings encountered in the inputs are to be replaced with the character "-"
def countSort(arr):
   new_arr= [""]
   for i in range(100):
       new_arr+= [""]
   for i in range(len(arr)):
       s = ""
       if(i<len(arr)//2):
           s = "- "
       else:
           s = arr[i][1] + " "
       k = int(arr[i][0])
       new_arr[k]+=s
   for i in new_arr:
       if i != "":
          print(i, end = "")

#try 20
#0 ab
#6 cd
#0 ef
#6 gh
#4 ij
#0 ab
#6 cd
#0 ef
#6 gh
#0 ij
#4 that
#3 be
#0 to
#1 be
#5 question
#1 or
#2 not
#4 is
#2 to
#4 the
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)