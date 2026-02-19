def Pattern(number: int)->str:
    '''  
    Return a descending number pattern string from number down to 1.
    Each row starts from the current number down to 1.
    '''
    result = ""  
    for x in range(number, 0, -1):      
        for i in range(x, 0, -1): 
            result += str(i) + " "  
        result += "\n"    
    return result  

print(Pattern(5))

print(Pattern.__doc__)






