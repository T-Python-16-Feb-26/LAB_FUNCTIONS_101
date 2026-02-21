def myfunction(number):
    ''' Prints a descending number pattern starting from n down to 1 '''
    result = ""         
    i = 1
    while i <= number:
        result += str(number) + " "
        number = number - i
    return result


number = int(input("Enter Your Number: "))

i = 1
pattern = ""             
while i <= number:
    pattern += "\n"      
    pattern += myfunction(number)
    number = number - i

print(pattern)
print(myfunction.__doc__)
