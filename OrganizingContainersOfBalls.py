#David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container.
# David wants to sort the balls using his sort method
#The distribution of ball types per container
# are described by an M[container][type] matrix of integers,
#David wants to perform some number of swap operations such that:
#-Each container contains only balls of the same type.
#-No two balls of the same type are located in different containers.
# print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible. 
def organizingContainers(container):
    all_sum= 0
    dict= {}
    for i in range(len(container)):
        for j in range(len(container)):
           all_sum += container[j][i]
           if i == 0:
               if sum(container[j]) not in  dict:
                  dict[sum(container[j])]= 1
               else:
                   dict[sum(container[j])]+=1
            
        if all_sum in dict:
            dict[all_sum]-= 1
            if dict[all_sum]<0:
                return "Impossible"
        else:
            return "Impossible"
        all_sum = 0
    return "Possible"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)
  

