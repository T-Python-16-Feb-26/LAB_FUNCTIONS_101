
def pattern_string (number:int)->str:
    to_string=""
    for s in range(number,0,-1):
        for s1 in range(s,0,-1):
            to_string+= str(s1) + " "
        to_string += "\n"
    return to_string

patternAsString= pattern_string(5)
print(patternAsString)