def Pattern(number:int):
    '''  
    Print a descending number pattern from number down to 1.
    Each row starts from the current number down to 1
    '''
    for x in range(number, 0, -1):      
        for i in range(x, 0, -1): 
            print(i, end=" ")
        print("\n" , end="")


Pattern(5)
print(Pattern.__doc__)