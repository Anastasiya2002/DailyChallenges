def biggerIsGreater(w):
    J= -1
    change = False
    for i in range(len(w)-1,0,-1):
            for j in range(i-1, J, -1): 
               if w[i] > w[j]:
                   I,J = i,j
                   change = True
                   break
    if change == False:
        return "no answer"
    return w[:J]+w[I] + ''.join(sorted(w[J:I]+w[I+1:]))




if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)
        print(result)
