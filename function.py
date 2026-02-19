def functions(a: int):
   ''' Prints a descending number pattern from the given integer to 1.'''

   for i in range(a, 0, -1):
       for j in range(i, 0, -1):
        print(j, end="  ")
       print()
functions(8)

print(functions.__doc__)