def string_pattern(n: int) -> str:
    ''' Prints string pattern '''

    pattern = ''

    for i in range(n, 0, -1):          
        for j in range(i, 0, -1):      
            pattern += str(j) + " "
        pattern += "\n"                

    return pattern

result = string_pattern(5)

print(result)
print(type(result))

print(string_pattern.__doc__)