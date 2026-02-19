def int_number(x:int):
    ''' this function takes an integer and draw stairs shape with it numbers '''
    while x != 0:
        for i in range(x,0,-1):
            print(i, end=" ")
        print("")
        x -= 1

int_number(5)
print(int_number.__doc__)