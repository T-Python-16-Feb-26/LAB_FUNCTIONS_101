def func(n:int):
    """this function takes an int number"""
    for i in range (n , 0, -1):
        for j in range (i,0,-1):
            print(j,end=" ")
        print()
func(9)
print(func.__doc__)

