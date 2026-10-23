koef_cost=0.85
koef_sav=0.15
def get_input(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("Ошибка:значение должно быть больше нуля")
        except ValueError:
            print("Ошибка типов")
income=get_input("Введите свой доход(в месяц):")
categ=["Жильё","Транспорт","Питание","Развлечения"]
costs={}
for k in categ:
    cost=get_input(f"Расходы на {k}(в месяц)")
    costs[k]=cost
expences=sum(costs.values())
print(f"Ваши общие расходы:{expences}")
savings=income-expences
print(f"Вы можете сберегать:{savings}")
if savings<0:
    print(f"Вы уходите в минус! Уменьшите свои расходы минимум на {expences-income}!")
elif income*koef_sav>=savings:
    print(f"Вы слишком мало сберегаете! Сберегайте минимум {income - income*koef_cost}!")
else:
    print(f"Вы сберегаете достаточную сумму")
most_categ=max(costs,key=costs.get)
if most_categ=="Жильё" or most_categ=="Транспорт" or most_categ=="Питание":
    print(f"Максимальное кол-во рассходов в категории:{most_categ}-{costs[most_categ]}, если есть возможность, стоим уменьшить ее расходы")
else:
    print(f"Максимальное кол-во рассходов в категории:{most_categ}-{costs[most_categ]}, вам нужно уменьшить расходы на ваши забавы")
costly_buy=get_input("Введите стоимость вашей дорогой покупки")
if savings<=0:
    print(f"Вы не можете накопить на свою цель, вы не сберегаете деньги!")
elif costly_buy/savings<=12:
    print(f"Вы можете накопить {costly_buy} за {costly_buy/savings} месяцев")
else:
    print(f"Вы можете накопить {costly_buy} за {costly_buy / savings} месяцев, однако это долгий период времени, потому найдите способ увеличить накопления")