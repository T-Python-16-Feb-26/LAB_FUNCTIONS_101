def pattern(rows):
    """
    This function prints a pattern of numbers where each row starts 
    from the current row number down to 1, separated by spaces.
    The number of rows is determined by the 'rows' parameter.

    """
    for i in range(rows, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

pattern(5)

print(pattern.__doc__)
