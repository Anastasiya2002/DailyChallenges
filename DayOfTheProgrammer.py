#gives a data of the holiday Day of Programmer for any year from 1700 to 2700
def dayOfProgrammer(y):
    if y == 1918:
        print("25.09"+ str(y))
        return
    if y % 4 == 0:
        print ("12.09."+str(y))
        return
    print("13.09." + str(y))

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    result
