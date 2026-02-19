def pyramid_pattern(num: int) -> str:
    """
    Return one row of the pyramid pattern from num down to 1 as a string.
    Example:
    >>> pyramid_pattern(5)
    '5 4 3 2 1'
    """
    pyramid_list = []
    for n in range(1, num + 1):
        pyramid_list.insert(0, n) 
    return " ".join(map(str, pyramid_list)) 

def cheak(num: int) -> str:
    """
    Return the full pyramid pattern from num down to 1 as a multi-line string.
    Each line contains descending numbers starting from the current row number down to 1.
    """
    result = ""
    while num != 0:
        result += pyramid_pattern(num) + "\n"  
        num -= 1
    return result  

# Get user input
user_number = int(input("Enter an integer number: "))
# Store the pattern in a variable
pattern = cheak(user_number)

# Print the final pattern
print(pattern)
