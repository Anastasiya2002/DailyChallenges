def generateParenthesis(n):
     def generate(A = []):
            print('Loop 1')
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
                    print('Added to result')
            else:
                A.append('(')
                print(A, "Added (")
                generate(A)
                print('At A generate')
                c = A.pop()
                print("popped" , c)
                A.append(')')
                print(A, "Added )")
                generate(A)
                print('At B generate')
                A.pop()

     def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

     ans = []
     generate()
     return ans

print(generateParenthesis(3))
        
    
