def pattern_function(num):
    """this function will return  the desired pattern of numbers as a string"""
    EndPattern=""
    for i in range(num,0,-1):
        j=i
        while j>0:
            EndPattern+=str(j)+" "
            j-=1
        EndPattern+="\n"
    return EndPattern

pattern=pattern_function(10)
print(pattern)
print(pattern_function.__doc__)
