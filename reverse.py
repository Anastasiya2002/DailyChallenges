def reverse(x: int) -> int:
        x = str(x)
        minus = False
        if x[0]== "-":
            minus = True
            x=x[1:]
        x= x[::-1]
        if minus:
            x= "-" + x
        x= int(x)
        if x > 2**31 or x < -2**31:
            return 0
        return x