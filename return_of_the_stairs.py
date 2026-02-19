def int_number(x:int):
    ''' this function takes an integer and draw stairs shape with it numbers '''
    string:str = ""
    while x != 0:
        for i in range(x,0,-1):
           string += str(i) + " "
        string += "\n"
        x -= 1
    return string

variable = int_number(5)
print(variable)
print(int_number.__doc__)