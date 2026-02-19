def descending_number(num:int):
    '''Create a function that takes 1 parameter of type int'''
    for i in range(num,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

user_input = int(input("Enter a number: "))
descending_number(user_input)

print(descending_number.__doc__)
