palin=input(f"Введите строку:").lower()
palin_is=1
for i in range(len(palin)//2):
    if palin[i]!=palin[len(palin)-1-i]:
        palin_is = 0
        break
if palin_is==0:
    print(f"Не палиндром")
else:
    print(f"Палиндром")