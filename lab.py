



def pattren (n):
    '''
    This is a function that print decassending numbers
    '''
    for i in range(n, 0 , -1):
        row = " "
        for j in range (i , 0, -1):
            row += str(j)
        print(row)

pattren(5)
print (pattren.__doc__)