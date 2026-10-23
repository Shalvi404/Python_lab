value=int(input(f"Введите количество денег в рублях:"))
nominal=[100,50,10,2,1]
count=[0,0,0,0,0]
for i in range(len(count)):
    while value//nominal[i]!=0:
        count[i]=count[i]+1
        value=value-nominal[i]
for i in range(len(count)):
    print(f"Купюр номиналом {nominal[i]}:{count[i]}")
