
def Pattern(num:int):
    for x in range(num, 0, -1):      
        for i in range(x, 0, -1): 
            print(i, end=" ")
        print("\n" , end="")


Pattern(5)


        