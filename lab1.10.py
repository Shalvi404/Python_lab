value=int(input(f"Введите цену:"))
birthday=input(f"Введите день рождения(**.**.****):").split(".")
today=input(f"Введите нынешний день(**.**.****):").split(".")
if int(birthday[0])>31 or int(birthday[1])>12 or int(today[0])>31 or int(today[1])>12:
    print(f"Ошибка:неправильная дата")
else:
    vip = input(f"VIP?(yes/no):")
    is_vip=vip.lower()=="yes"
    age = int(today[2]) - int(birthday[2])
    discount = 0.0
    if age >= 63:
        discount += 0.05
    if value >= 1000:
        discount += 0.1
    if today[0] == birthday[0] and today[1] == birthday[1]:
        discount += 0.05
    if is_vip and discount>0.15:
        discount = max(discount,0.15)
    print(f"Итоговая цена:{value - discount * value:.2f}")
    print(f"Итоговая скидка:{discount}")