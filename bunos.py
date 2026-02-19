
def number(x:int):
    y= ""
    for i in range(x,0,-1):
        for j in range(i,0,-1):
          y+= (str(j)+'  ')
        y +=('\n')
    return y 
    

print(number(5))