def functions(a: int):
    '''Returns a descending number pattern from the given integer down to 1 as a string'''

    result = ""

    for i in range(a, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result += "\n"

    return result

pattern = functions(8)
print(pattern)

print(functions.__doc__)
