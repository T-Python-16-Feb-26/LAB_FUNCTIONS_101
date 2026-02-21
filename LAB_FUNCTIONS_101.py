


def myfunction(number):
    ''' Prints a descending number pattern starting from n down to 1 '''
    i = 1
    while i <= number:
        print(number, end=" ")
        number = number - i



number = int(input("Enter Your Number: "))
i=1
while i <= number:
    print("")
    myfunction(number)
    number = number - i
print("")
print(myfunction.__doc__)
    