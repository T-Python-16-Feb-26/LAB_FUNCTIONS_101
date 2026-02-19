def print_pattern(n: int):
    ''' prints a pattern of numbers'''

    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

print_pattern(5)
print(print_pattern.__doc__)


