def Josephus(m,n):
    s_list = [i for i in range(1,n+1)]
    idx=-1
    while len(s_list) > 2:
        idx +=m
        if idx > len(s_list)-1:
            idx -= len(s_list)
        del s_list[idx]
        idx -=1
    return s_list
