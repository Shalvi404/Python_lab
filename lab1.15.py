wholeprod=[]
while True:
    name=input(f"Введите название товара:")
    if not name:
        break
    try:
        value=float(input(f"Введите цену товара:"))
        count = int(input(f"Введите кол-во товара:"))
    except ValueError:
        print(f"Неверный тип данных")
        break
    tovar={
        "name":name,
        "value":value,
        "count":count
           }
    wholeprod.append(tovar)

total_sum=0
total_max=0
name_of_max='nothing'
for i in wholeprod:
    delta=i.get("value",0)*i.get("count",0)
    total_sum=total_sum+delta
    if delta>total_max:
        total_max=delta
        name_of_max=i.get("name","nothing")
every_tovar={prod.get("name","") for prod in wholeprod}
print(f"Общая прибыль:{total_sum}")
print(f"Максимально прибыльный товар:{name_of_max}")
print(f"Уникальных имен:{len(every_tovar)}")