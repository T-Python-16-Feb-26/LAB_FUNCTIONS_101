def make_tower(num:int):    
    tower_string = ""
    temp = ""
    list = []
    for i in range(1, num+1):
        temp = str(i) + " " + temp
        list.append(temp)
    for i in range(len(list)-1, -1, -1):
        tower_string += list[i] + "\n"
    return tower_string

my_tower = make_tower(5)
print(my_tower)