def print_pattern(n: int):
  """Print a descending number pattern from n down to 1 in multiple lines."""
  for i in range(n, 0, -1):
        for j in range(i, 0, -1):
             print(j, end=" ")
        print()

print_pattern(5)

def pattern_as_string(n: int) -> str:
    """Return the same descending number pattern as a single string."""
    result = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result += "\n"
    return result


output = pattern_as_string(5)
print(print_pattern.__doc__)

print(output)




