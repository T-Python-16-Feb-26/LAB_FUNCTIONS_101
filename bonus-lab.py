def pyramidFunction(n):
    
    '''
    Docstring for pyramidFunction
    this funtion takes a number n and prints a pyramid of numbers with n levels but as a string variable
    :param n: the input which determines the size of the pyramid
    '''
    var4print =""
    num =n
    for i in range(1, n+1):
        for j in range(1, num+1):
            var4print += f' {num} '
            num -= 1
            
        var4print += "\n"
        num = n - i
    return var4print

if int(input("chose to use the function or get docs on it, 1 for using the function, 2 for getting docs:")) == 1:
    print(pyramidFunction(int(input("enter the number of levels for the pyramid:"))))
elif 2:
    print(pyramidFunction.__doc__)
else:
    print("invalid input")