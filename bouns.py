


def pattren(n):
    '''
     This is a function that print decassending numbers as string
    '''
    result =""

    for i in range(n , 0, -1):
        for j in range(i , 0 , -1):
           result += str(j) 
        result += "\n"
    return result 

 
p_result = pattren(5)
print (p_result)
print (pattren.__doc__)