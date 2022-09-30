list_1 = [1,3,2,8,4,7,5,6]
s_list = [] 

popped = list_1.pop()
s_list.append(popped)
for i in list_1:
    s_list.append(i)
    ind = s_list.index(i)
    ind_b = ind - 1
    while(s_list[ind_b] > s_list[ind]):
        a = s_list[ind]
        b = s_list[ind_b]
        s_list[ind_b] = a
        s_list[ind] = b
        ind = s_list.index(i)
        ind_b = ind - 1
        if(ind_b == -1):
            break
        
print(s_list)        