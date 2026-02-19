def pattern_number (number:int):
    '''A function that prints numbers in a descending pyramid pattern'''
    for n in range(number,0,-1):
        for n1 in range(n, 0,-1):
            print(n1, end= " ")
        print()
        
pattern_number(5)
print(pattern_number.__doc__)

