def func(n:int) -> str:
    """returns the pattern as string"""
    result=" "
    for i in range (n , 0, -1):
      for j in range (i,0,-1):
          result += f"{j} "
      result += "\n"
    return result
output = func(9)
print(output)