def pattern_function(num):
    """this function will print the desired pattern of numbers"""
    for i in range(num,0,-1):
        j=i
        while j>0:
            print(j ,end=" ")
            j-=1
        print()

pattern_function(10)
print()
print(pattern_function.__doc__)
