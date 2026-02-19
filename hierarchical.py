#Lab
def hierarchical_num(n:int)->int:

    '''
    generate a hierarchical number as int
    this function create a hierarchical num like this below:
    if n=5 the output will be:
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
    
    '''
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j, end=" ")
        
        print()


hierarchical_num(5)

help(hierarchical_num)



#bouns
def hierarchical_num2(n:int)->str:
    '''
    generate a hierarchical number as string
    this function create a hierarchical num like this below:
    if n=5 the output will be:
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1


    '''


    result=""

    
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            result+=str(j)+ " "
        
        result+="\n"
    return result




#x=hierarchical_num2(5)

#print(x)


help(hierarchical_num2)
