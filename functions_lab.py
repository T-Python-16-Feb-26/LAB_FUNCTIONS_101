

def pattern_of_num(n): 
    '''prints number pattern starting from n to 1 
    creating a nested loop'''
    
    i = n
    while i >= 1:
        x = 1
        while x <= i:
            print(x, end=" ")
            x += 1
        print()
        i -= 1

pattern_of_num(5)
print(pattern_of_num.__doc__)
