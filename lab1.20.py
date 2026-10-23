def list_transform(list_b):
    i=0
    while len(list_b)>i:
        if type(list_b[i]) is list:
            list_transform(list_b[i])
            list_b[i:i+1]=list_b[i]
        else:
            i+=1
def list_unique(list_b):
    list_unique=[]
    for i in list_b:
        if i not in list_unique:
            list_unique.append(i)
    return list_unique
list_a=[1,2,[1,2,[1,2,[0,2,3,4,1]]]]
list_transform(list_a)
list_c=list_unique(list_a)
print(list_c)