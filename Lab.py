def number(num:int)->int:
    '''Create a function that takes 1 parameter of type int'''
    for i in range(num,0,-1):
        print(end="\n")
        for j in range(i,0,-1):
            print(j,end=" ")

user_input = int(input("Enter a number: "))
number(user_input)

print("\n",number.__doc__)
