def make_tower(num:int):
    """takes 1 parameter of type int, prints out the result formatted as a tower """
    for i in range(num, 0, -1):
        temp = ""
        for j in range(i, 0, -1):
            temp += str(j) + " "
        print(temp)

make_tower(5)
print(make_tower.__doc__)