def pyramid_pattern(num: int):
    """
    Print one row of the pyramid pattern from num down to 1.
    Example:
    If num = 5, it prints: 5 4 3 2 1
    """
    pyramid_list = []
    for n in range(1, num + 1):
        pyramid_list.insert(0, n)
    print(*pyramid_list)

def cheak(num: int):
    """
    Print the full pyramid pattern from num down to 1.
    Calls pyramid_pattern for each row starting from num down to 1.
    """
    while num != 0:
        pyramid_pattern(num)
        num -= 1

# Get user input
number = int(input("Enter integer number: "))

# Call function to print the pyramid pattern
cheak(number)
