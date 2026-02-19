def pattern_as_string(n: int) -> str:
    """
       Completed the bonus requirements:
    """
    result = ""

    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result += "\n"

    return result
pattern = pattern_as_string(5)
print(pattern)

print(pattern_as_string.__doc__)