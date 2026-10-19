def list_transform(list_b):
    i=0
    while len(list_b)>i:
        if type(list_b[i]) is list:
            list_transform(list_b[i])
            list_b[i:i+1]=list_b[i]
        else:
            i+=1
list_a=[1,2,[1,2,[1,2,[0,1]]]]
list_transform(list_a)
print(list_a)