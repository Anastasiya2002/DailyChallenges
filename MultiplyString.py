#You must not use any built-in BigInteger library or convert the inputs to integer directly.
def multiply(self, num1: str, num2: str) -> str:
        return str(self.s_to_i(num1)*self.s_to_i(num2))
		
def s_to_i(self, num):
        c = 0
        sum = 0
        for j in reversed(num):
            n = (10**c) * int(j)
            sum = sum + n
            c = c + 1
        return sum
