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
    print(var4print)

pyramidFunction(5)