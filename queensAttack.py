#check how many steps can queen make 
#n: an integer, the number of rows and columns in the board
#k: an integer, the number of obstacles on the board
#r_q: integer, the row number of the queen's position
#c_q: integer, the column number of the queen's position
#obstacles: a two dimensional array of integers where each element is an array of 2 integers,
def queensAttack(n,k,r_q,c_q,obstacles):
    count = 0
    found = False
    difference = r_q-c_q
    count += (n-1)+(n-1)
    if r_q > n//2 and c_q > n//2:
            r_q =n-r_q +1
            c_q = n-c_q +1
    if n % 2 ==1:
        count += 2*(n - 1 - abs(r_q-c_q))
    else:
        count += (n -abs(r_q-c_q))+ (n - 1 - abs(r_q-c_q))

    for i in range(1,n+1):
        #to find obstacles on horizontal
        if [r_q,i] in obstacles:
            count -= i
        #to find obstacles on vertical
        if [i,c_q] in obstacles:
            count -=i
    return count
    
        

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)